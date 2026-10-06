---
title: 'Coding standards'
description: 'Documentation on team coding standards'
---


<sup>*Introduced via [gitlab-com/support/support-ops/support-ops-project#1963](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/1963)*</sup>

This document defines coding standards and best practices to follow for the GitLab Customer Support Systems team. By utilizing these guidelines, we ensure consistency, maintainability, simplicity, and better collaboration within the team. All contributors to our projects are expected to follow these guidelines, unless a specific exception is agreed upon.

## General Principles

We believe the [GitLab core values](/handbook/values/) should guide all our coding decisions:

- Collaboration
  - Collaborate with teammates, review each other’s code, and share knowledge.
  - Always be open to feedback and improve your code based on it.
  - Ensure your contributions are readable and understandable to others on the team
- Results
  - Focus on the impact and effectiveness of the code.
  - Prioritize working solutions over perfect solutions (but try to avoid shortcuts that undermine quality)
- Efficiency
  - Write clear and maintainable code.
  - Strive for simplicity without sacrificing functionality.
- Transparency
  - Code should be easy to understand and accessible to all.
  - Document assumptions, choices, and design decisions clearly when needed.
- Iteration
  - Code should be flexible and easy to refactor.
  - We aim for continuous improvement and don't shy away from updating or reworking code when necessary.

## Naming Conventions

- Variables
  - Use descriptive names that clearly convey the purpose of the variable. If the name of the variable does not clearly convey the purpose, then add a comment on the code to explain it better.
  - All variable names should use snake case:
    - Examples: `sum_of_pairings`, `gitlab_user`
- Constants
  - Use descriptive names that clearly convey the purpose of the constant. If the name of the constant does not clearly convey the purpose, then add a comment on the code to explain it better.
  - Constants should be written in upper snake case:
    - Examples: `MAX_RETRIES`, `DEFAULT_TIMEOUT`
- Functions and Methods
  - Function and method names should describe the action they perform. If the name of the function/method does not clearly convey the purpose, then add a comment on the code to explain it better.
  - Function and method names should be written in snake case
    - Examples: `my_new_function`, `check_gitlab_user`
- Classes and Modules
  - Classes and modules should be written in PascalCase:
    - Examples: `AccountBlocked`, `SupportSuperFormProcessor`
- Filenames
  - All filenames should use snake case:
    - Examples: `process_account`, `compare_only`

## Code Formatting

- Indentation
  - Use 2 spaces per indentation level whenever possible.
    - Example:

      ```ruby
      def self.subscriptions
        @subscriptions ||= Readiness::GitLab::Namespaces.subscription(client, namespace)
      end
      ```

- Line length
  - Keep lines of code to a maximum length of 80-120 characters (aim for 80, maximum is 120). This ensures readability and allows code to fit comfortably in most environments.
- Blank lines
  - Use blank lines to separate functions, classes, and logically related code blocks
  - Use a single blank line between method definitions
- Spacing
  - Use a single space between operators (e.g. `+`, `<`, `=`, etc.)

## Comments and Documentation

- Inline comments
  - Use inline comments sparingly. Only use them to clarify complex or non-obvious code. If you need a large number of comments, you are probably overcomplicating your code!
  - Keep comments up to date and relevant to the code they describe.

## Code Complexity

- Avoid deeply nested code. Refactor code to use helper functions or early returns if nesting becomes too complex.
- Limit function size. Each function should have a clear, single responsibility and be relatively small (under 20 lines).

## Testing

Always aim for high test coverage! When in doubt, test your code thoroughly!

## Version control

- Commit messages
  - Detail the changes being made
  - Add text to relate it to the issue you are working out of
  - Example:

    ```plaintext
    Adding new attribute "title" to article object

    Relates to https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/1963
    ```

- Branches
  - The format of a branch should follow the format of `USERNAME-PROJECT-IID`,
    where:
    - `USERNAME` is your gitlab.com username
    - `PROJECT` is the project's slug
    - `IID` is the issue's IID
    - Example:
      - For branch `jcolyer` is creating for the work of issue `https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/1963`, your branch name should be `jcolyer-support-ops-project-1963`

## Use semantic versioning

{{% alert title="Note" color="primary" %}}

- This is a generalization. For more specifics on versioning, see the documentation page for the item you are working on.

{{% /alert %}}

Whenever you need to use version numbers, you should strive to use semantic versioning, which is in the format of `MAJOR.MINOR.PATCH`.

When increasing the version number, you should use the following to determine which number to increase:

- Increase the `MAJOR` if you do a sizable refactor
- Increase the `MINOR` if you add or remove functionality
- Increase the `PATCH` if you are making small changes (wording changes, bug fixes, etc.)

Remember, when increasing a value:

- If increasing `MAJOR`, the new values of `MINOR` and `PATCH` are 0
- If increasing `MINOR`, the new value `PATCH` are 0 (and `MAJOR` remaining unchanged)
- If increasing `PATCH`, the values of `MAJOR` and `MINOR` remain unchanged

To help you, here are some examples:

| Starting Version | `MAJOR` update | `MINOR` update | `PATCH` update |
|------------------|----------------|----------------|----------------|
| `1.0.0`          | `2.0.0`        | `1.1.0`        | `1.0.1`        |
| `1.9.127`        | `2.0.0`        | `1.10.0`       | `1.9.128`      |
| `2.99.0`         | `3.0.0`        | `2.100.0`      | `2.99.1`       |
| `9.99.9`         | `10.0.0`       | `9.100.0`      | `9.99.10`      |

### Using semantic versioning when only two numeric values are allowed

If you are working with something only allowed two numeric values (such as `1.01` or `9.8`), you would instead combine the definitions of `MINOR` and `PATCH` for the second value. This results in the needed format of `xx.yy` and allows you to maintain a close semblance to semantic versioning.

Thus, when increasing the version number, you should use the following to determine which number to increase:

- Increase the `xx` if you do a sizable refactor
- Increase the `yy` if you add or remove functionality, or if you are making small changes (wording changes, bug fixes, etc.)

To help you, here are some examples:

| Starting Version | `MAJOR` update | `MINOR`/`PATCH` update |
|------------------|----------------|------------------------|
| `1.0`            | `2.0`          | `1.1`                  |
| `1.9`            | `2.0`          | `1.10`                 |
| `2.99`           | `3.0`          | `2.100`                |
| `9.99`           | `10.0`         | `9.100`                |

## Error Handling

Whenever possible, have your code gracefully handle errors. Where this is not possible, ensure the errors clearly explain what the problem is (and bonus points if they tell you what to do about it).

## Performance Considerations

- Focus on performance only after your code is functional and maintainable. Avoid premature optimization.
- Measure performance impacts using profiling tools and identify bottlenecks before optimizing.
- Use common sense to reduce API calls to our tooling.
  - Example: While you could manually fetch every ticket from Zendesk one by one, there is no logical reason to when the Readiness Gem will do this efficiently using the `list` method.

## Security

- Validate all inputs to prevent injection attacks (e.g., SQL Injection, XSS).
- Never store passwords, tokens, etc. in plaintext. Use CI/CD variables.

## Code Reviews

- All code must undergo peer review before merging. Ensure reviews are thorough and address quality, consistency, and security.
- Embrace constructive feedback and improve the code collaboratively.

## Language specific guidelines

This currently focuses on our primary language, ruby. This is a living section and more should be added for other languages we might use in the future.

### Ruby

- Whenever possible, try to ensure your code presents no issues when run via the [rubocop](https://rubygems.org/gems/rubocop) linter.

## Examples to help you get started

### Writing a ruby script

When writing a ruby script, it is recommended you start with:

<details>
<summary>Click to expand</summary>

```ruby
#!/usr/bin/env ruby
# frozen_string_literal: true

require 'active_support'
require 'active_support/time'
require 'base64'
require 'erb'
require 'faraday'
require 'json'
require 'yaml'

class ApiResponseError < StandardError; end
class ApiAuthenticationError < ApiResponseError; end
class ApiForbiddenError < ApiResponseError; end
class ApiNotFoundError < ApiResponseError; end
class ApiRateLimitError < ApiResponseError; end
class ApiServerError < ApiResponseError; end
class SafeUpdateError < ApiResponseError; end

def debug
  ENV.fetch('DEBUG', false)
end

def sandbox?
  ENV.fetch('SANDBOX', false).to_s == 'true'
end

def max_retries
  @max_retries ||= ENV.fetch('MAX_RETRIES', 3).to_i
end

def base_retry_delay
  @base_retry_delay ||= ENV.fetch('BASE_RETRY_DELAY', 2).to_i
end

def request_timeout
  @request_timeout ||= ENV.fetch('REQUEST_TIMEOUT', 60).to_i
end

def open_timeout
  @open_timeout ||= ENV.fetch('OPEN_TIMEOUT', 15).to_i
end

def page_size
  @page_size ||= ENV.fetch('PAGE_SIZE', 100).to_i
end

def unexpected_response_message(response)
  body = response.body if response.respond_to?(:body) && !response.body.to_s.empty?
  "Unexpected response: HTTP #{response.status}#{" - #{body}" if body}"
end

def handle_response(response, allowed_statuses: [])
  return response if response.status.between?(200, 299)
  return response if allowed_statuses.include?(response.status)

  handle_error_status(response)
end

def handle_error_status(response)
  case response.status
  when 401 then raise ApiAuthenticationError, 'Authentication failed - check your credentials'
  when 403 then raise ApiForbiddenError, 'Access forbidden - insufficient permissions'
  when 404 then raise ApiNotFoundError, 'Resource not found'
  when 409 then raise SafeUpdateError, 'Safe update conflict'
  when 429 then handle_rate_limit(response)
  when 500..599 then raise ApiServerError, "Server error: HTTP #{response.status}"
  else raise ApiResponseError, unexpected_response_message(response)
  end
end

def handle_rate_limit(response)
  retry_after = response.headers['retry-after']&.to_i || 60
  raise ApiRateLimitError, "Rate limited - retry after #{retry_after}s"
end

def request_with_retry(client, method, url, params = {}, allowed_statuses: []) # rubocop:disable Metrics/MethodLength
  attempt = 0
  response = nil

  begin
    attempt += 1
    response = execute_request(client, method, url, params, allowed_statuses)
  rescue ApiRateLimitError, ApiServerError, Faraday::TimeoutError, Faraday::ConnectionFailed, Faraday::SSLError => e
    handle_retryable_error(e, attempt) && retry
  rescue SafeUpdateError => e
    raise SafeUpdateError, e
  rescue StandardError => e
    handle_fatal_error(e, response)
  end
end

def execute_request(client, method, url, params, allowed_statuses)
  response = make_request(client, method, url, params)
  handled_response = handle_response(response, allowed_statuses: allowed_statuses) # rubocop:disable Style/HashSyntax
  return nil if handled_response.nil?

  handle_body(response.body, response.headers['content-type'])
end

def handle_retryable_error(error, attempt)
  return handle_rate_limit_error(error, attempt) if error.is_a? ApiRateLimitError
  return retry_request(attempt, error.message) if error.is_a? ApiServerError
  return retry_request(attempt, "Timeout: #{error.message}") if error.is_a? Faraday::TimeoutError
  return retry_request(attempt, "Connection failed: #{error.message}") if error.is_a? Faraday::ConnectionFailed
  return retry_request(attempt, "SSL error: #{error.message}") if error.is_a? Faraday::SSLError

  true
end

def handle_rate_limit_error(error, attempt)
  if error.message.match(/retry after (\d+)s/)
    sleep_time = Regexp.last_match(1).to_i
    puts "⏳ Rate limited, waiting #{sleep_time}s..."
    sleep(sleep_time)
  end
  retry_request(attempt, error.message)
end

def handle_fatal_error(error, response)
  puts "❌ #{format_error_message(error)}"
  puts "[DEBUG] BODY: #{response&.body}" if debug && response
  print_backtrace(error) if should_print_backtrace?(error)
  exit 1
end

def format_error_message(error)
  case error
  when ApiResponseError
    "API Error: #{error.message}"
  else
    "Unexpected error: #{error.message}"
  end
end

NON_BACKTRACE_ERRORS = [
  ArgumentError,
  ApiAuthenticationError,
  ApiForbiddenError,
  ApiNotFoundError,
  ApiResponseError
].freeze

def should_print_backtrace?(error)
  NON_BACKTRACE_ERRORS.none? { |error_class| error.is_a?(error_class) }
end

def print_backtrace(error)
  error.backtrace.each { |line| puts "  #{line}" }
end

def handle_body(body, content_type = nil)
  return body if body.nil? || body.empty?

  if content_type&.include?('application/json') || content_type.nil?
    JSON.parse(body)
  else
    body
  end
rescue JSON::ParserError
  body
end

def make_request(client, method, url, params)
  case method.to_sym
  when :get, :delete
    client.public_send(method.to_sym, url, params)
  when :post, :put, :patch
    client.public_send(method.to_sym, url) do |r|
      r.body = determine_body_type(client, params)
    end
  else
    raise ArgumentError, "Unsupported HTTP method: #{method}"
  end
end

def determine_body_type(client, params)
  return params if params.is_a?(String)
  return '' if params.nil?

  content_type = client.headers['Content-Type']&.downcase
  return URI.encode_www_form(params) if content_type&.include?('application/x-www-form-urlencoded')

  params.to_json
end

def retry_request(attempt, error_msg)
  if attempt < max_retries
    delay = base_retry_delay * (2**(attempt - 1))
    sleep(delay)
    true
  else
    puts "❌ Failed after #{max_retries} attempts: #{error_msg}"
    exit 1
  end
end

def extract_next_url(next_url)
  return nil if next_url.nil? || next_url.empty?

  uri = URI.parse(next_url)
  relative_url = uri.path
  relative_url += "?#{uri.query}" if uri.query
  relative_url
rescue => e # rubocop:disable Style/RescueStandardError
  puts "❌ Invalid pagination URL: #{e.message}"
  exit 1
end

def safe_update(client, method, url, &update_block)
  request_with_retry(client, method, url, update_block.call)
rescue SafeUpdateError
  print 'update conflict, waiting 2 seconds and retrying...'
  sleep 2
  retry
end
```

</details>

This ensures you can start coding on the very next line and have a good starting point to work from.

#### Making a request

Using the [starting code](#writing-a-ruby-script), you can make an external request like so:

<details>

<summary>Simple GET request</summary>

```ruby
page_data = request_with_retry(client_variable, :get, url_to_use)
```

</details>
<details>
<summary>Request with a payload</summary>

```ruby
payload = {
  'text' => 'Jason is awesome',
  'reason' => 'Cause I said so'
}
page_data = request_with_retry(client_variable, :post, url_to_use, payload)
```

</details>
<details>
<summary>Request with a payload using safe_update</summary>

```ruby
def update_object
  {
    'subject' => 'New subject',
    'updated_stamp' => DateTime.now.utc.iso8601,
    'safe_update' => true
  }
end

page_data = safe_update(client_variable, :put, url_to_use) { update_object }
```

</details>
<details>
<summary>Simple GET request allowing a 404 response</summary>

```ruby
page_data = request_with_retry(client_variable, :get, url_to_use, allow404: true)
```

</details>

As a more complete example, here we have code to fetch all automations for a Zendesk instance:

<details>
<summary>Click to expand</summary>

```ruby
print 'Fetching Zendesk automations'

@automations = []
url = "api/v2/automations?page[size]=#{page_size}"
loop do
  print '.'
  page_data = request_with_retry(zendesk_client, :get, url)
  @automations += page_data['automations']
  break unless page_data['meta']['has_more']

  url = extract_next_url(page_data.dig('links', 'next'))
end

puts 'done! ✅ Successfully fetched Zendesk automations!'
```

</details>

### Connecting to Zendesk via ruby

When you need to connect to Zendesk, use the [starting point](#writing-a-ruby-script) and then add the following:

<details>
<summary>For Zendesk Global</summary>

```ruby
def base_url
  sandbox? ? 'https://gitlab1707170878.zendesk.com' : 'https://gitlab.zendesk.com'
end

def zendesk_secret
  return ENV.fetch('SB_ZD_SECRET') if sandbox?

  ENV.fetch('ZD_SECRET')
end

def zendesk_client_name
  return ENV.fetch('SB_ZD_CLIENT_NAME') if sandbox?

  ENV.fetch('ZD_CLIENT_NAME')
end

def zendesk_bearer_token
  @zendesk_bearer_token ||= generate_zendesk_bearer_token
end

def generate_zendesk_bearer_token
  client = Faraday.new(base_url) do |f|
    f.options.timeout = request_timeout
    f.options.open_timeout = open_timeout
    f.headers['Content-Type'] = 'application/json'
  end
  url = 'oauth/tokens'
  response = request_with_retry(client, :post, url, zendesk_bearer_token_payload)
  response['access_token']
end

def zendesk_bearer_token_payload
  {
    'client_id' => zendesk_client_name,
    'client_secret' => zendesk_secret,
    'grant_type' => 'client_credentials',
    'scope' => 'read write'
  }
end

def setup_zendesk_client
  Faraday.new(base_url) do |f|
    f.options.timeout = request_timeout
    f.options.open_timeout = open_timeout
    f.headers['Content-Type'] = 'application/json'
    f.headers['Authorization'] = "Bearer #{zendesk_bearer_token}"
  end
end

def zendesk_client
  @zendesk_client ||= setup_zendesk_client
end

def zendesk_oauth_client
  oauth_clients = []
  url = "api/v2/oauth/clients?page[size]=#{page_size}"
  loop do
    page_data = request_with_retry(zendesk_client, :get, url)
    oauth_clients += page_data['clients']
    break unless page_data['meta']['has_more']

    url = extract_next_url(page_data.dig('links', 'next'))
  end
  oauth_clients.detect { |o| o['identifier'] == zendesk_client_name }
end

def revoke_token!
  url = "api/v2/oauth/tokens?client_id=#{zendesk_oauth_client['id']}"
  tokens = request_with_retry(zendesk_client, :get, url)
  token = tokens['tokens'].detect { |t| t['token'] == "...#{zendesk_bearer_token[-10..]}" }
  return if token.nil?

  request_with_retry(zendesk_client, :delete, "api/v2/oauth/tokens/#{token['id']}")
end

def find_in_collection(collection, attribute, value, collection_name)
  print "[DEBUG] Locating #{collection_name} from #{value}..." if debug

  item = collection.detect { |obj| obj[attribute].to_s.downcase == value.to_s.downcase }
  if item.nil?
    puts "❌ Unable to locate matching #{collection_name}" if debug
    raise "Cannot find #{collection_name} #{value}"
  end

  puts "done! ✅ Successfully determined #{collection_name}!" if debug
  item
end
```

</details>
<details>
<summary>For Zendesk US Government</summary>

```ruby
def base_url
  sandbox? ? 'https://gitlabfederalsupport1585318082.zendesk.com' : 'https://gitlab-federal-support.zendesk.com'
end

def zendesk_secret
  return ENV.fetch('US_SB_ZD_SECRET') if sandbox?

  ENV.fetch('US_ZD_SECRET')
end

def zendesk_client_name
  return ENV.fetch('US_SB_ZD_CLIENT_NAME') if sandbox?

  ENV.fetch('US_ZD_CLIENT_NAME')
end

def zendesk_bearer_token
  @zendesk_bearer_token ||= generate_zendesk_bearer_token
end

def generate_zendesk_bearer_token
  client = Faraday.new(base_url) do |f|
    f.options.timeout = request_timeout
    f.options.open_timeout = open_timeout
    f.headers['Content-Type'] = 'application/json'
  end
  url = 'oauth/tokens'
  response = request_with_retry(client, :post, url, zendesk_bearer_token_payload)
  response['access_token']
end

def zendesk_bearer_token_payload
  {
    'client_id' => zendesk_client_name,
    'client_secret' => zendesk_secret,
    'grant_type' => 'client_credentials',
    'scope' => 'read write'
  }
end

def setup_zendesk_client
  Faraday.new(base_url) do |f|
    f.options.timeout = request_timeout
    f.options.open_timeout = open_timeout
    f.headers['Content-Type'] = 'application/json'
    f.headers['Authorization'] = "Bearer #{zendesk_bearer_token}"
  end
end

def zendesk_client
  @zendesk_client ||= setup_zendesk_client
end

def zendesk_oauth_client
  oauth_clients = []
  url = "api/v2/oauth/clients?page[size]=#{page_size}"
  loop do
    page_data = request_with_retry(zendesk_client, :get, url)
    oauth_clients += page_data['clients']
    break unless page_data['meta']['has_more']

    url = extract_next_url(page_data.dig('links', 'next'))
  end
  oauth_clients.detect { |o| o['identifier'] == zendesk_client_name }
end

def revoke_token!
  url = "api/v2/oauth/tokens?client_id=#{zendesk_oauth_client['id']}"
  tokens = request_with_retry(zendesk_client, :get, url)
  token = tokens['tokens'].detect { |t| t['token'] == "...#{zendesk_bearer_token[-10..]}" }
  return if token.nil?

  request_with_retry(zendesk_client, :delete, "api/v2/oauth/tokens/#{token['id']}")
end

def find_in_collection(collection, attribute, value, collection_name)
  print "[DEBUG] Locating #{collection_name} from #{value}..." if debug

  item = collection.detect { |obj| obj[attribute].to_s.downcase == value.to_s.downcase }
  if item.nil?
    puts "❌ Unable to locate matching #{collection_name}" if debug
    raise "Cannot find #{collection_name} #{value}"
  end

  puts "done! ✅ Successfully determined #{collection_name}!" if debug
  item
end
```

</details>

You should make sure to run the function `revoke_token!` at the end of your script (or when API connections are no longer needed).

### Connecting to GitLab.com via ruby

When you need to connect to GitLab, use the [starting point](#writing-a-ruby-script) and then add the following:

<details>
<summary>Click to expand</summary>

```ruby
def gitlab_token
  ENV.fetch('GL_TOKEN')
end

def setup_gitlab_client
  Faraday.new('https://gitlab.com') do |f|
    f.options.timeout = request_timeout
    f.options.open_timeout = open_timeout
    f.headers['Content-Type'] = 'application/json'
    f.headers['Authorization'] = "Bearer #{gitlab_token}"
  end
end

def gitlab_client
  @gitlab_client ||= setup_gitlab_client
end
```

</details>

### Connecting to Slack via ruby

When you need to connect to Slack, use the [starting point](#writing-a-ruby-script) and then add the following:

<details>
<summary>Click to expand</summary>

```ruby
def slack_client
  @slack_client ||= Faraday.new(ENV.fetch('SLACK_URL')) do |f|
    f.options.timeout = request_timeout
    f.options.open_timeout = open_timeout
    f.headers['Content-Type'] = 'application/json'
  end
end
```

</details>

You can then use this to make requests. An example of this:

<details>
<summary>Make a Slack post using an incoming webhook</summary>

```ruby
payload = { 'text' => 'I am a slack post!' }
request_with_retry(slack_client, :post, '', payload)
```

</details>

### Connecting to Salesforce via ruby

When you need to connect to Salesforce, use the [starting point](#writing-a-ruby-script) and then add the following:

<details>
<summary>Click to expand</summary>

```ruby
def base_salesforce_url
  'https://login.salesforce.com'
end

def instance_url
  'https://gitlab.my.salesforce.com'
end

def salesforce_client_id
  ENV.fetch('SFDC_CLIENTID')
end

def salesforce_client_secret
  ENV.fetch('SFDC_CLIENTSECRET')
end

def salesforce_username
  ENV.fetch('SFDC_USERNAME')
end

def salesforce_password
  ENV.fetch('SFDC_PASSWORD')
end

def salesforce_security_token
  ENV.fetch('SFDC_SECURITYTOKEN')
end

def initial_connection
  @initial_connection ||= Faraday.new(base_salesforce_url) do |c|
    c.options.timeout = request_timeout
    c.options.open_timeout = open_timeout
    c.headers['Accept'] = 'application/json'
    c.headers['Content-Type'] = 'application/x-www-form-urlencoded'
    c.request :url_encoded
  end
end

def bearer_token
  @bearer_token ||= generate_token_with_retry
end

def salesforce_client
  @salesforce_client ||= Faraday.new(instance_url) do |c|
    c.options.timeout = request_timeout
    c.options.open_timeout = open_timeout
    c.headers['Content-Type'] = 'application/json'
    c.headers['Authorization'] = "Bearer #{bearer_token}"
  end
end

def generate_token_with_retry
  data = {
    'grant_type' => 'password',
    'client_id' => salesforce_client_id,
    'client_secret' => salesforce_client_secret,
    'username' => salesforce_username,
    'password' => "#{salesforce_password}#{salesforce_security_token}"
  }
  url = 'services/oauth2/token'
  page_data = request_with_retry(initial_connection, :post, url, data)
  page_data['access_token']
end
```

</details>

You can then use this to make requests. Some examples of this:

<details>
<summary>Make a SOQL query</summary>

```ruby
encoded_query = URI.encode_www_form_component("SELECT Name FROM Account WHERE Id = 'ABC123'")
url = "services/data/v58.0/query/?q=#{encoded_query}"
page_data = request_with_retry(salesforce_client, :get, url)
```

</details>
<details>
<summary>Create a Case in Salesforce</summary>

```ruby
payload = {
  'AccountId' => 'ABC123',
  'Description' => 'I am a case',
  'OwnerId' => 'DEF456',
  'RecordTypeId' => 'GHI321',
  'Subject' => 'New case!'
}
case_id = 'XYZ789'
url = "services/data/v58.0/sobjects/Case/#{case_id}"
page_data = request_with_retry(salesforce_client, :post, url, payload)
```

</details>

### Connecting to Mailgun via ruby

When you need to connect to Mailgun, use the [starting point](#writing-a-ruby-script) and then add the following:

<details>
<summary>Click to expand</summary>

```ruby
def mailgun_token
  ENV.fetch('MAILGUN_KEY')
end

def setup_mailgun_client
  Faraday.new("https://api:#{mailgun_token}@api.mailgun.net") do |f|
    f.options.timeout = request_timeout
    f.options.open_timeout = open_timeout
    f.request :multipart
    f.request :url_encoded
  end
end

def mailgun_client
  @mailgun_client ||= setup_mailgun_client
end
```

</details>

You can then use this to make requests. Some examples of this:

<details>
<summary>Send an email</summary>

```ruby
payload = {
  'from' => 'Bob Smith <bsmith@example.com>',
  'to' => 'jsmith@example.com',
  'subject' => 'Awesome boats',
  'text' => "Hey Jenny\n\nHere is a list of awesome boats!"
}
page_data = request_with_retry(mailgun_client, :post, url, payload)
```

</details>

### Connecting to Google via ruby

#### Google Sheets

When you need to connect to Google Sheets, use the [starting point](#writing-a-ruby-script) and then add the following:

<details>
<summary>Click to expand</summary>

```ruby
def initial_connection
  @initial_connection ||= Faraday.new('https://oauth2.googleapis.com/token') do |c|
    c.options.timeout = request_timeout
    c.options.open_timeout = open_timeout
    c.headers['Content-Type'] = 'application/x-www-form-urlencoded'
  end
end

def bearer_token
  @bearer_token ||= generate_token_with_retry
end

def google_client
  @google_client ||= Faraday.new('https://sheets.googleapis.com/v4') do |f|
    f.options.timeout = request_timeout
    f.options.open_timeout = open_timeout
    f.headers['Content-Type'] = 'application/json'
    f.headers['Authorization'] = "Bearer #{bearer_token}"
  end
end

def generate_token_with_retry
  signature_input = "#{jwt_encoded_header}.#{jwt_encoded_claim_set}"
  private_key = OpenSSL::PKey::RSA.new(@service_account['private_key'])
  signature = private_key.sign(OpenSSL::Digest.new('SHA256'), signature_input)
  encoded_signature = Base64.urlsafe_encode64(signature, padding: false)
  data = {
    'grant_type' => 'urn:ietf:params:oauth:grant-type:jwt-bearer',
    'assertion' => "#{signature_input}.#{encoded_signature}"
  }
  page_data = request_with_retry(initial_connection, :post, '', data)
  page_data['access_token']
end

def jwt_encoded_header
  Base64.urlsafe_encode64({ alg: 'RS256', typ: 'JWT' }.to_json, padding: false)
end

def jwt_encoded_claim_set
  Base64.urlsafe_encode64(claim_set.to_json, padding: false)
end

def claim_set
  now = Time.now.to_i
  {
    iss: @service_account['client_email'],
    scope: 'https://www.googleapis.com/auth/spreadsheets',
    aud: 'https://oauth2.googleapis.com/token',
    exp: now + 3600,
    iat: now
  }
end

@service_account = JSON.parse(File.read('PATH_TO_CREDENTIALS_FILE'))
```

</details>

You can then use this to make requests. Some examples of this:

<details>
<summary>List entries in a Google Sheet</summary>

```ruby
spreadsheet_id = 'ID_TO_USE'
range = "'NAME_OF_SHEET'!A500"
url = "spreadsheets/#{spreadsheet_id}/values/#{ERB::Util.url_encode(range)}"
page_data = request_with_retry(google_client, :get, url)
```

</details>
<details>
<summary>Add entries in a Google Sheet</summary>

```ruby
spreadsheet_id = 'ID_TO_USE'
range = "'NAME_OF_SHEET'!A500"
data = {
  'values' => [
    [ 'Jenny', '867-5309', 'jenny@example.com' ]
  ]
}
url = "spreadsheets/#{spreadsheet_id}/values/#{ERB::Util.url_encode(range)}?valueInputOption=RAW"
request_with_retry(google_client, :put, url, data)
```

</details>
<details>
<summary>Clear entries in a Google Sheet</summary>

```ruby
spreadsheet_id = 'ID_TO_USE'
range = "'NAME_OF_SHEET'"
url = "spreadsheets/#{spreadsheet_id}/values/#{ERB::Util.url_encode(range)}:clear"
request_with_retry(google_client, :post, url)
```

</details>

#### Google Calendars

When you need to connect to Google Calendars, use the [starting point](#writing-a-ruby-script) and then add the following:

<details>
<summary>Click to expand</summary>

```ruby
def initial_connection
  @initial_connection ||= Faraday.new('https://oauth2.googleapis.com/token') do |c|
    c.options.timeout = request_timeout
    c.options.open_timeout = open_timeout
    c.headers['Content-Type'] = 'application/x-www-form-urlencoded'
  end
end

def bearer_token
  @bearer_token ||= generate_token_with_retry
end

def google_client
  @google_client ||= Faraday.new('https://www.googleapis.com/calendar/v3') do |f|
    f.options.timeout = request_timeout
    f.options.open_timeout = open_timeout
    f.headers['Content-Type'] = 'application/json'
    f.headers['Authorization'] = "Bearer #{bearer_token}"
  end
end

def generate_token_with_retry
  signature_input = "#{jwt_encoded_header}.#{jwt_encoded_claim_set}"
  private_key = OpenSSL::PKey::RSA.new(@service_account['private_key'])
  signature = private_key.sign(OpenSSL::Digest.new('SHA256'), signature_input)
  encoded_signature = Base64.urlsafe_encode64(signature, padding: false)
  data = {
    'grant_type' => 'urn:ietf:params:oauth:grant-type:jwt-bearer',
    'assertion' => "#{signature_input}.#{encoded_signature}"
  }
  page_data = request_with_retry(initial_connection, :post, '', data)
  page_data['access_token']
end

def jwt_encoded_header
  Base64.urlsafe_encode64({ alg: 'RS256', typ: 'JWT' }.to_json, padding: false)
end

def jwt_encoded_claim_set
  Base64.urlsafe_encode64(claim_set.to_json, padding: false)
end

def claim_set
  now = Time.now.to_i
  {
    iss: @service_account['client_email'],
    scope: 'https://www.googleapis.com/auth/calendar',
    aud: 'https://oauth2.googleapis.com/token',
    exp: now + 3600,
    iat: now
  }
end

@service_account = JSON.parse(File.read('PATH_TO_CREDENTIALS_FILE'))
```

</details>

You can then use this to make requests. Some examples of this:

<details>
<summary>Listing events on a calendar</summary>

```ruby
Time.zone = TZInfo::Timezone.get('America/Los_Angeles')
params = [
  'maxResults=100',
  'orderBy=startTime',
  'singleEvents=true',
  "timeMin=#{Time.zone.now.beginning_of_day.iso8601}",
  "timeMax=#{Time.zone.now.end_of_day.iso8601}",
  "timeZone=#{Time.zone.name}"
]
calendar_id = 'ID_TO_USE'
url = "calendars/#{calendar_id}/events?#{params.join('&')}"
page_data = request_with_retry(google_client, :get, url)
```

</details>
<details>
<summary>Creating an event on a calendar</summary>

```ruby
Time.zone = TZInfo::Timezone.get('America/Los_Angeles')
payload = {
  'description' => 'Meeting between Alice and Bob',
  'start' => {
    'dateTime' => '2025-12-18T08:00:00-07:00',
    'timeZone' => 'America/Los_Angeles'
  },
  'end' => {
    'dateTime' => '2025-12-18T08:25:00-07:00',
    'timeZone' => 'America/Los_Angeles'
  },
  'location' => 'zoom_link_goes_here'
}
calendar_id = 'ID_TO_USE'
url = "calendars/#{calendar_id}/events"
request_with_retry(google_client, :post, url, payload)
```

</details>
