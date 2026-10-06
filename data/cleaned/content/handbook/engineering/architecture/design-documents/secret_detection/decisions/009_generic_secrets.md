---
title: "GitLab Secret Detection ADR 009: Detecting Generic Secrets"
---

This ADR outlines the approach for detecting unstructured secrets and sensitive credential types that fall outside of [Rule-based coverage](https://docs.gitlab.com/user/application_security/secret_detection/detected_secrets/).

## Context

Generic Secrets detection was initially explored through an [experiment](https://gitlab.com/groups/gitlab-org/-/work_items/18502) by the Vulnerability Research team for detecting high-entropy strings. The experiment consisted of specialized detectors, with each detector designed to independently identify whether a given string has high entropy. The Secret Detection team then borrowed certain concepts from the experiment to develop the `Entropy engine` workflow for detecting generic secrets.

## Scope

The Entropy engine's primary scope is to identify literals in the scan payload that would appear to be potential secrets **syntactically** based on their occurrence at certain areas (_hotspots_) along with appropriate context (e.g., sensitive keywords around them). The engine should exclude syntactically safe strings, such as variable name references, from identified literals. Evaluating whether literals are potential secrets based on their **semantics** (i.e., the intent of the literal, such as whether it is a placeholder or test value) is outside the scope of the engine.

## Solution

Unlike Rule-based regex scan engines, generic secrets do not have pre-defined patterns to extract exact secret values from the payload. We extract string literals from specific areas (_hotspots_) where generic secrets are likely to appear, then analyze the extracted contents. Sometimes, extracted string literals are just random values like variable name references. We apply multiple techniques using the extracted value and surrounding context to filter out literals with random values.

The Entropy engine detects Generic Secrets through three stages:

1. **Literal Extraction**: Extract all possible string literals from areas in the target payload where secrets might appear.
2. **Type Evaluation**: Determine the underlying type of extracted literals (e.g., JWT, Base64Encoded) to run type-specific operations such as format validation and decoding.
3. **Filtration**: Apply filters in the post-extraction step to remove random values extracted as literals before returning the engine result.

High level illustration of entropy engine stages:

![Entropy Engine](/images/engineering/architecture/design-documents/secret_detection/009_generic_secrets.jpeg "Entropy Engine")

### Secret Categories

Before we go further into the details of Generic Secrets detection stages, let us understand a bit about secrets.

A typical Secret exhibits different properties (e.g. entropy, case-switch ratio, dictionary words, etc.) which makes it difficult to have one common set of rules to evaluate any literal as secret. For example, `superhuman@123` is a false positive for an API token while a potential true positive for a DB password. This is why we need to categorize them and have a specific set of rules applicable for each category.

Technically, secrets are generated using one of these two methods, each exhibiting specific properties:

1. **Machine-generated**: High entropy. High case-switch ratio. Small-sized (<=3 chars) to no dictionary words. No longer (>3) repeated sequences. Typically longer strings.

2. **Human-generated**: Mostly opposite to machine generated strings with visible human signals like the usage of common dictionary words. Character repetitions/sequences. Low case-switch ratio.

These method-specific properties would help us define specific rules for evaluating literals. However, it is not always possible to determine whether a secret is machine- or human-generated from its value alone. We need to look beyond the value itself, using signals inferred from the surrounding context.

Based on the nature of secrets, we came up with the following secret categories:

- **Password**: Any secrets that are defined by humans. Typical signals for human-defined passwords are secrets assigned to variable names containing "pass", "password", or "pwd" keywords, and also the password section in the URI strings.

- **API Key** : Vendor-specific secrets. Typical signals include the usage of vendor/their product names in the surrounding context. E.g. `aws_secret_key = "..."` or sometimes in nested structures like `{"aws": {"secret_key": "..." }}`.

- **Cryptographic Key**: These are multi-line secrets, typically certificates and private keys with fixed prefix/suffix formats.

- **Generic**: This is the misc category representing scenarios when the secret exhibits properties but NO useful signals to deduce a specific category from its surrounding context. For instance, `var SECRET = "2m49dn2-1Z3-rM2-4Q32"`.

### Literal Extraction

This is the first stage of generic secrets detection. We extract string literals from specific areas (hotspots) in the scan payload where secrets are more likely to appear as one of their [categories](#secret-categories). Common hotspots include variable assignments, dictionary assignments, URL parameters, CLI flags, connection URIs, authorization bearer tokens, and comments.

There are two popular approaches to literal extraction:

1. **Regex-based Extraction**: A dedicated regex pattern for each hotspot type. Pros: Minimal effort, low engineering complexity, covers most scenarios, language-agnostic. Cons: Brittle, prone to false positives and false negatives in certain scenarios.

2. **AST-based Extraction**: Parse the AST tree of the payload and extract literals via AST queries. Pros: Higher accuracy, robust, low maintenance burden. Cons: Language-specific (requires grammars), less accurate if the payload's language cannot be determined, increased binary size for larger grammar support, higher resource consumption for larger payloads unless streamed.

Both approaches have distinct strengths and weaknesses. The AST-based approach doesn't work for scan payloads with plaintext content or missing language information, making the Regex-based approach a necessary fallback. Therefore, the Regex-based approach is essential regardless of whether we adopt the AST-based approach.

We decided to use the Regex-based approach first, then implement the AST-based approach for popular languages only to reduce binary size, combining the benefits of both approaches. We create a regex pattern for each hotspot to extract literals matching a specific secret category. For example, to extract passwords, we define an assignment-like expression where the Left Hand Side (LHS) contains keywords like `password`, `pwd`, or `pass`, and the Right Hand Side (RHS) is a string literal.

### Literal Type Evaluation

While the extraction stage extracts and categorizes literals into one of the [secret categories](#secret-categories), this stage determines their underlying format (aka Literal Type, e.g., JWT, Base64Encoded, Hex) regardless of secret category. This step is necessary to find secrets hidden in plaintext. For example, a JWT token might appear less critical until we discover a secret key in its decoded contents. Identifying literal types also enables type-specific treatment, as entropy thresholds differ between JWTs and UUID strings.

We currently identify the following formats:

- `UUID`
- `Base64`
- `Base64URL`
- `JWT`
- `JWE`
- `Paseto`
- `Hex`
- `AlphaNum`
- `ASCII`
- `Raw` (Undetermined; Default)

### Filtration

Even literals extracted from hotspots and assigned to high-confidence keywords like `key`, `token`, or `secret` can still be false positives. For instance, variable references in the value or unintended matches (e.g., `var primaryKeyName = "transaction_id"` or `TOKEN_SOURCE=https://stripe.com/webhook/test`).

We capture the literal, its category, underlying type, and surrounding context to determine sensitivity. We use multiple filtration techniques including filtering by value (absolute/relative file paths, URLs, array/dict access, environment variable access), LHS variable name keywords (e.g., signing, primary, column), and file path keywords (e.g., node_modules/, docs/, vendor/).

This stage filters out extracted literals that are unlikely to be secrets and returns the remaining literals as the Entropy engine's final scan results.

## Generic Secrets in Encoded Literals

Identifying the literal type opens up an opportunity to search for secrets within encoded literals that support decoding, such as Base64, URL-encoded, and JWT formats. We decode these literals and then check for hotspots within the decoded contents by running the detection workflow recursively once.

## Future Scope

### AST-based Literal Extraction

As mentioned in the [Literal Extraction](#literal-extraction) section, we plan to implement AST-based extraction to complement the existing regex-based approach. This will provide higher accuracy for supported languages while maintaining regex-based extraction as a fallback.

### ML Integration

Future iterations will explore integrating machine learning models to enhance detection accuracy:

- **Context-aware Classification**: Use ML models to better understand the intent behind variable assignments and string usage patterns
- **False Positive Reduction**: Train models on historical detection data to identify patterns that commonly result in false positives
- **Adaptive Thresholds**: Dynamically adjust entropy thresholds based on file context, language, and historical patterns

### Supporting More Encoding Detections

Expand support for detecting secrets hidden in various encoding formats:

- **Custom Base Encodings**: Support for Base32, Base85, and other encoding schemes
- **Nested Encoding**: Detect secrets that are encoded multiple times (e.g., Base64 of URL-encoded strings)
- **Compression Detection**: Identify secrets within compressed data formats
