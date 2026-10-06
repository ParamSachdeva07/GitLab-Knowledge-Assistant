---
layout: handbook-page-toc
title: "ADR 007: Attestations for private repositories, GitLab dedicated and self-managed instances"
description: "This ADR establishes the mechanisms through which software attestations can be achieved in situations where public Sigstore infrastructure cannot be used."
---

## Background

The ~"group::pipeline security" group is working towards providing users with
[SLSA Level 3 Provenance Attestations](/handbook/engineering/architecture/design-documents/slsa_level_3/).
As a simplified summary, in the [context of GitLab](/handbook/engineering/architecture/design-documents/slsa_level_3/),
a provenance statement is a JSON document that correlates the SHA-256 sum of an
artifact or an OCI container with the build information. A worker then performs a
[digital signature](/handbook/engineering/architecture/design-documents/slsa_level_3/decisions/004_attestation_in_sidekiq/),
called a provenance attestation, stored as a "Sigstore Bundle" blob.

These digital signatures are kicked off by the background worker, but they
leverage what is known as the "public-good" Sigstore infrastructure. More
information is available in the [Sigstore Overview](https://docs.sigstore.dev/about/overview/)
page. This "public-good" infrastructure is not suitable for private
repositories, and self-managed and dedicated deployments for reasons highlighted
below.

This ADR captures our decision to perform signatures using a key stored within
PostgreSQL, and documents our rationale for doing so. Additionally, this ADR
contains information regarding our decision to temporarily disable Rekor in
these cases, while a permanent decision is made regarding its usage.

Additionally, it highlights the new UX our users will leverage in order to use
this functionality, as well as what technical mechanisms will be used in this
integration.

### Why this change is required

The points highlighted below, specifically the disclosure of information to
Rekor and the difficulty of the integration with Sigstore for self-managed and
Dedicated deployments, show that our current implementation is not viable for
these kinds of customers.

By implementing the changes in this ADR, we are able to provide SLSA L3
attestations in the control plane by leveraging already existing infrastructure
in a cost-effective way. By using the proposed solution our users are able to
easily configure their pipelines to generate attestations which can then be
verified before consumption, preventing supply chain attacks for our most
security conscious users.

### References

- [[Discussion] UX to enable SLSA provenance generation (#547903)](https://gitlab.com/gitlab-org/gitlab/-/work_items/547903#note_2748278333)
- [ADR 002: Generate SLSA Provenance in GitLab Rails backend](/handbook/engineering/architecture/design-documents/slsa_level_3/decisions/002_provenance_generation_location/)
- [ADR 006: Enable the creation of SLSA Level 3 Attestations for OCI images](https://gitlab.com/gitlab-com/content-sites/handbook/-/merge_requests/17936)
- [Cosign Image Signatures. The protocol format explained!](https://medium.com/sigstore/cosign-image-signatures-77bab238a93)
- [FF `slsa_provenance_statement` -- Roll out feature flag to publish SLSA provenance statements (#547866)](https://gitlab.com/gitlab-org/gitlab/-/work_items/547866)
- [Phase 5: OCI Containers Attestation (#20683) · Epic · gitlab-org](https://gitlab.com/groups/gitlab-org/-/work_items/20683)
- [Signing artifacts, attesting builds, and why you should do both](https://some-natalie.dev/blog/signing-attesting-builds/)
- [SLSA • Build: Requirements for producing artifacts](https://slsa.dev/spec/v1.2/build-requirements)
- [SLSA • Provenance](https://slsa.dev/spec/v1.1/provenance)
- [SLSA Level 3 Provenance Attestations](/handbook/engineering/architecture/design-documents/slsa_level_3/)
- [OpenBao chart | GitLab Docs](https://docs.gitlab.com/charts/charts/openbao/)
- [GitLab Secrets Manager (OpenBao) | GitLab Docs](https://docs.gitlab.com/administration/secrets_manager/#openbao-architecture)

## Desired user experience (UX)

Changes will be required to the UX specified in the [SLSA level 3 provenance attestations](https://docs.gitlab.com/ci/pipeline_security/slsa/level_3/)
page.

A new environment variable will be created, which will control whether to use a
local CA. This optional variable, `ATTEST_METHOD`, accepts two possible values:
`SIGSTORE`, or `LOCAL_CA`. This value defaults to `SIGSTORE` for public projects
in GitLab.com, and `LOCAL_CA` for private repositories, GitLab dedicated and
self-managed.

Specifically, the new UX will look as follows:

```yaml
build-job:
  stage: build
  variables:
    ATTEST_BUILD_ARTIFACTS: true
    ATTEST_METHOD: LOCAL_CA
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"
    - echo "Hello, $GITLAB_USER_LOGIN!" > test.txt
  artifacts:
    paths:
      - test.txt
```

Here's an example of the UX with the optional value not included. In this case
the behavior will be to use the default value.

```yaml
build-job:
  stage: build
  variables:
    ATTEST_BUILD_ARTIFACTS: true
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"
    - echo "Hello, $GITLAB_USER_LOGIN!" > test.txt
  artifacts:
    paths:
      - test.txt
```

Users of this feature can override this default value. The rationale for
allowing users to override this value is twofold. Firstly, this gives users who
are able to use Sigstore in a self-managed instance the choice to use Sigstore.
Secondly, making this value explicit allows us to add other values, such as
other BYOK providers.

Our current behavior is to disallow `SIGSTORE` for private projects, which will
be preserved.

## Technical background

Largely, the Sigstore public good infrastructure authenticates with OIDC, and
then if the authentication is successful, performs a signature. The identity of
the signature, will be dependent on what identity is used to authenticate
against that OIDC server. An example of an identity would be a username or
email, although in this process we authenticate as a repository/branch
combination.

The threat model clarifies what the signature means:

> Under normal operation (no Sigstore compromise), verifying a "keyless" signature from `user@example.com` using the ExampleIdP identity provider at a given timestamp guarantees that the signature was created by a signer who successfully authenticated to Sigstore using that identity at that time.

### On the usage of the above mechanism for private repositories on GitLab.com

While this is suitable for public projects, where the artifacts and container
images are known to the public and not sensitive, private projects within
GitLab.com may not wish to disclose this information publicly. Here is an
example attestation for a container: [Rekor Search](https://search.sigstore.dev/?uuid=108e9186e8c5677a23c91a821a2732ffad83e22d730c98dee8af822aaaaac5fe512fdc8eabebc6fd).
Information disclosed is: hash of the binary, name of the organization, name of
the project, name of the repository and builder, among other details.

As of this point, the assumption is that disclosure of information is acceptable
for public projects, but unacceptable for private projects. Due to this, we've
gated the code to only perform attestations when the project is public.

### On the usage of the above mechanism for self-managed and dedicated deployments

In addition to the point above about information disclosure for private
projects, there is an additional constraint that prevents the usage of
"public-good" Sigstore infrastructure for self-managed and dedicated
deployments.

In the explanation above, there is a mention of the "OpenID Provider". These are
restricted by default, and Fulcio maintains an allowlist. In the case of
GitLab.com, we've performed specific work to ensure our OIDC provider is added
to the list, as tracked in the "[Use GitLab.com as an OIDC provider for cosign (#10254)](https://gitlab.com/groups/gitlab-org/-/work_items/10254)"
ticket.

In the case of self-managed and dedicated deployments, each of our customers
would need to create an MR similar to [this one](https://github.com/sigstore/fulcio/pull/1327)
in order for their instance to be allowed. This is not practical or advisable to
do, and the changes highlighted in this ADR would prevent our customers from
having to go through this process.

### On Rekor

#### What is Rekor

From: [An Introduction to Rekor — Chainguard Academy](https://edu.chainguard.dev/open-source/sigstore/rekor/an-introduction-to-rekor/):

> Rekor stores records of artifact metadata, providing transparency for
> signatures and therefore helping the open source software community monitor
> and detect any tampering of the software supply chain. On a technical level,
> it is an append-only (sometimes called "immutable") data log that stores
> signed metadata about a software artifact, allowing software consumers to
> verify that a software artifact is what it claims to be. You could think of
> Rekor as a bulletin board where anyone can post, and the posts cannot be
> removed, but it's up to the viewer to make informed judgements about what to
> believe.ct's lifecycle.
> [...]
> Users of Rekor also have an offline method for determining whether a
> particular entry exists in a Rekor log by leveraging inclusion proofs, which
> are enabled through Merkle trees. Merkle trees are a data structure that
> enable a party to use cryptographic hash functions — a way of mapping
> potentially large values to relatively short digests — to prove that a piece
> of data is contained within a much larger data structure. This proof is
> accomplished by providing a series of hashes to the user, hashes that if
> recombined prove to the user that an entry is indeed in the Rekor log.
> Sigstore users can "staple" such an inclusion proof to an artifact, attaching
> the inclusion proof next to an artifact in a repository, and therefore proving
> that the artifact is indeed included in Rekor. For a detailed description of
> Merkle trees and inclusion proofs, refer to the helpful resources section at
> the end of this chapter.

Key characteristics of Rekor are:

- Immutable
- Tamper-resistant

More information on the role that Rekor plays in public infrastructure is
available in the [Threat Model](https://docs.sigstore.dev/about/threat-model/)
page. Additional research into Rekor, and how to potentially replicate that behavior
in-house, can be found in the [Explore designs for multi-tenant attestations (#21881)](https://gitlab.com/groups/gitlab-org/-/work_items/21881)
page.

#### Is use of an immutable, tamper-resistant log a requirement for SLSA L3?

There is an additional [potential requirement around a replacement for Rekor](https://gitlab.com/gitlab-org/gitlab/-/work_items/590549#note_3326516370).
Fundamentally though, the use of Rekor is associated with the usage of Sigstore
and not a requirement under SLSA L3. The only two requirements exclusive to L3
are "Unforgeable", and "Isolated":

- **Unforgeable**: Provenance MUST be strongly resistant to forgery by tenants.
- **Isolated**: The build platform ensured that the build steps ran in an isolated environment, free of unintended external influence.

More discussion in https://gitlab.com/gitlab-org/gitlab/-/work_items/590549#note_3326516370

## Decision: Perform signing using a key stored in PostgreSQL

A full discussion of the options reviewed can be found on the "[Investigate Options for self-managed/customer owned Sigstore. (#590549)](https://gitlab.com/gitlab-org/gitlab/-/work_items/590549)"
ticket.

After carefully reviewing our options, considering aspects such as complexity of
implementation, ease of use for our customers, as well as security and other
aspects, we've decided to:

- Perform signing using a key stored in PostgreSQL and intermediate, ephemeral
  keys. More detail below.
- Hold off on the decision to implement a tamper-resistant log of attestations,
  based on the discussion [in this comment](https://gitlab.com/gitlab-org/gitlab/-/work_items/590549#note_3326516370).
  In the meantime, we will disable Rekor until a decision is made on the issue.

### Key generation, rotation and revocation

At a high-level, there will be two types of keys in this solution:

- Certificate Authority (CA) keys.
- Intermediate, ephemeral keys used for signing the attestations.

The root CA keys will be stored within a new model,
`SupplyChain::SigningCertificate`. Handling of these keys will be done in
accordance with the [Secure coding development guidelines](https://docs.gitlab.com/development/secure_coding_guidelines/#handling-credentials),
specifically the "Handling Credentials" section, as private keys are explicitly
mentioned there. These guidelines indicate that when the value needs to be
retrieved in plaintext, it should be stored as an [application secret](https://docs.gitlab.com/development/application_secrets/).
This is done similarly in other parts of the codebase, such as
the `Clusters::Platforms::Kubernetes` class's `ca_cert` attribute. Also,
relevant to this decision are the [GitLab Cryptography Standard](/handbook/security/policies_and_standards/cryptographic-standard/) and
the [Encryption Standard](https://internal.gitlab.com/handbook/security/policies_and_standards/standards/encryption-standard/).
Any solution implemented by this ADR will follow these documents.

Key rotation can be achieved by having multiple keys being present within the
`SupplyChain::SigningCertificate` model. Because verification will accept a
signature by any of the keys within that table, a transitionary period can be
implemented where multiple keys are valid. After clients have migrated to use
the new key, the old key can be revoked. Similarly, key revocation can be
handled by removing keys from the table. Old attestations can also be signed
with new keys if required.

Example code on how to create a CA is available in the [CA Certificate section of the OpenSSL documentation](https://ruby.github.io/openssl/OpenSSL.html#module-openssl-ca-certificate).
Please see the example below. Please note that the example below uses RSA keys,
but this does not mean that we should be using that specific key type in our
implementation. Our implementation will adhere to the policies linked above and
as such may vary in its choice of key type.

```ruby

# Generate the key.
# WARNING: Choose the right key type taking into consideration the policies above
ca_key = OpenSSL::PKey::RSA.new 2048 # Stored in SupplyChain::SigningCertificate

ca_name = OpenSSL::X509::Name.parse '/CN=ca/DC=example'

ca_cert = OpenSSL::X509::Certificate.new
ca_cert.serial = 0
ca_cert.version = 2
ca_cert.not_before = Time.now
ca_cert.not_after = Time.now + 86400

ca_cert.public_key = ca_key.public_key
ca_cert.subject = ca_name
ca_cert.issuer = ca_name

extension_factory = OpenSSL::X509::ExtensionFactory.new
extension_factory.subject_certificate = ca_cert
extension_factory.issuer_certificate = ca_cert

ca_cert.add_extension \
  extension_factory.create_extension('subjectKeyIdentifier', 'hash')
ca_cert.add_extension \
  extension_factory.create_extension('basicConstraints', 'CA:TRUE', trues
```

### Generation of ephemeral keys for signing

An intermediate, ephemeral key will be generated for each attestation. The
public key associated with the key will be persisted within the
`SupplyChain::Attestation` model.

```ruby
# Generate the key. Choose the right key type based on the considerations above.
key = OpenSSL::PKey::RSA.new 2048
name = OpenSSL::X509::Name.parse '/CN=#{sanitised_ci_ref_uri}/DC=gitlab'

cert = OpenSSL::X509::Certificate.new
cert.version = 2
cert.serial = 0
cert.not_before = Time.now
cert.not_after = Time.now + 3600

cert.public_key = key.public_key
cert.subject = name
```

`cert`, above, can be signed with `ca_cert` as follows. `SHA1` is only
an example and the appropriate digest should be chosen instead.

```ruby
# Choose the appropriate digest to use instead of SHA1.
cert.sign ca_key, OpenSSL::Digest.new('SHA1')
```

The key can be used for signing a provenance with the instructions provided by
`cosign` in the [Signing with Self-Managed Keys](https://docs.sigstore.dev/cosign/key_management/signing_with_self-managed_keys/)
page.

### Signature verification

The verification of a signature can be performed manually, or through
GitLab's `glab` tool. Calling `glab` will look identical to how it is documented
in the [SLSA level 3 provenance attestations](https://docs.gitlab.com/ci/pipeline_security/slsa/level_3/#verifying-attestations)
page. For example:

```bash
glab attestation verify gitlab-org/gitlab filename.txt
```

Code for this command-line endpoint is available at [internal/commands/attestation/verify/verify.go](https://gitlab.com/gitlab-org/cli/-/blob/main/internal/commands/attestation/verify/verify.go).
This will be modified slightly for key verification.

This tool will do the following:

1. Get the project metadata.
2. Calculate the digest of the artifact/container.
3. Retrieve the provenance metadata, with the [Attestations API](https://docs.gitlab.com/api/attestations/).
   This metadata will be indicative of whether the verification needs to happen
   with Sigstore or with the solution indicated in this ADR. If the latter is
   true, the endpoint will return the signed public key associated with the
   ephemeral key.
4. Retrieve the bundle associated with the attestation.
5. Retrieve a list of valid Certificate Authorities.

With this information, we will perform the following verifications.

1. We will call the `cosign` binary referencing the key and bundle file,
   similarly to how we verify with Sigstore. This will ensure the provenance is
   signed by the key associated with it.
2. We will ensure the ephemeral key is signed by a valid "Root CA". This will be
   done with the information returned by step 5 above.
3. We will ensure the `subject` field matches the `ci_ref_uri` of the
   repository. This field is documented in [OpenID Connect (OIDC) Authentication Using ID Tokens](https://docs.gitlab.com/ci/secrets/id_token_authentication/).

Step 1 can be completed with the instructions provided in the [Signing with Self-Managed Keys](https://docs.sigstore.dev/cosign/key_management/signing_with_self-managed_keys/)
page. Steps 2 and 3 can be achieved with the following code in Ruby:

```ruby
cert.verify ca_key.public_key
=> true
cert.subject == name
=> true
```

An attacker without access to this key cannot generate a valid certificate for
repositories they cannot control. This is because the CN of the certificate is
set to `ci_ref_uri` and the certificate is generated using the `ca_key`, which
is securely stored in the database.

To clarify, if a user generates a `SupplyChain::Attestation` for `RepoA` and
`main` branch, this will have a different subject to the one generated for
`MaliciousRepo` `main` branch. This ensures that if a user does not have write
access to the specific branch, the attestations generated by our system for
other branches cannot be used to bypass verification procedures.

### Positive Consequences

- No external dependencies for this feature, it is entirely self-contained.
- Would work well in combination with
  [BYOK](https://gitlab.com/gitlab-org/gitlab/-/work_items/590549#note_3326459572)
  in a future iteration, because we will create appropriate abstractions that
  will ensure this.
- Relatively small engineering footprint and cost.
- Does not require any new services to be created or maintained.
- Supports all environments and all repository types.

### Negative Consequences

- Does not include a solution in terms of a tamper-proof, immutable record of
  signatures, such as Rekor. This is a temporary situation until a permanent
  solution is found. See [this comment](https://gitlab.com/gitlab-org/gitlab/-/work_items/590549#note_3326516370)
  for more information.

## Testing, Performance and Availability

To ensure high-levels of availability and robust performance, several
measures will be put in place by the SSCS stage's Pipeline Security team:

- Manual testing of the attestation process in production behind a feature flag,
  to prevent accidental impacts to other GitLab users.
- End-to-end tests for our `cosign` integration will provide assurance
  for our `cosign` upgrade.
- We will implement extensive test coverage, particularly for failure scenarios.
  This will ensure the appropriate measures are in place to allow for the
  graceful handling of outages.
- Sidekiq jobs will be configured to retry as appropriate to ensure that sporadic
  outages do not lead to persistent failures in SLSA attestation generation.
- This feature will only be enabled for users who specifically opt-in.
- We will use Sidekiq's default [retry configuration](https://docs.gitlab.com/development/sidekiq/#retries) for
  dealing with transient failures. We have also flagged our worker as having
  [external dependencies](https://docs.gitlab.com/development/sidekiq/worker_attributes/#jobs-with-external-dependencies).
