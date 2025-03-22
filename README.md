# Google Contacts MCP Server

This server provides a pure MCP implementation for Google Contacts API integration. It allows you to manage Google Contacts through a standardized MCP interface with natural language responses.

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a Google Cloud Platform project
4. Enable the Google People API
5. Create OAuth 2.0 credentials (desktop application) and download the JSON file

## Credentials Setup

The server will automatically try to load credentials in the following order:

1. **From command-line arguments**:
   ```bash
   python main.py --client-id="your-client-id" --client-secret="your-client-secret" --refresh-token="your-refresh-token"
   ```
   
   Or with a credentials file:
   ```bash
   python main.py --credentials-file="/path/to/credentials.json"
   ```

2. **From environment variables**:
   ```bash
   export GOOGLE_CLIENT_ID="your-client-id"
   export GOOGLE_CLIENT_SECRET="your-client-secret"
   export GOOGLE_REFRESH_TOKEN="your-refresh-token" # Optional, only if you have an existing token
   ```

3. **From default file locations**:
   - ~/.config/google/credentials.json
   - ~/google_credentials.json
   - ./credentials.json (in the same directory as the script)

## Running the Server

```bash
# Run with stdio transport (default)
python main.py

# Run with HTTP transport
python main.py --transport=http --host=localhost --port=8000
```

## Command-line Options

```
usage: main.py [-h] [--transport {stdio,http}] [--host HOST] [--port PORT]
               [--client-id CLIENT_ID] [--client-secret CLIENT_SECRET]
               [--refresh-token REFRESH_TOKEN] [--credentials-file CREDENTIALS_FILE]

MCP Google Contacts Server

options:
  -h, --help            show this help message and exit
  --transport {stdio,http}
                        Transport protocol to use (default: stdio)
  --host HOST           Host for HTTP transport (default: localhost)
  --port PORT           Port for HTTP transport (default: 8000)
  --client-id CLIENT_ID
                        Google OAuth client ID (overrides environment variable)
  --client-secret CLIENT_SECRET
                        Google OAuth client secret (overrides environment variable)
  --refresh-token REFRESH_TOKEN
                        Google OAuth refresh token (overrides environment variable)
  --credentials-file CREDENTIALS_FILE
                        Path to Google OAuth credentials.json file
```

## Available Tools

The following MCP tools are available:

1. **List Contacts**
   - Tool name: `list_contacts`
   - Parameters: 
     - `name_filter` (optional): Filter contacts by name
     - `max_results` (optional): Maximum number of results to return

2. **Get Contact**
   - Tool name: `get_contact`
   - Parameters:
     - `identifier`: Resource name (people/*) or email address

3. **Create Contact**
   - Tool name: `create_contact`
   - Parameters:
     - `given_name`: First name
     - `family_name` (optional): Last name
     - `email` (optional): Email address
     - `phone` (optional): Phone number

4. **Update Contact**
   - Tool name: `update_contact`
   - Parameters:
     - `resource_name`: Contact resource name
     - `given_name` (optional): Updated first name
     - `family_name` (optional): Updated last name
     - `email` (optional): Updated email
     - `phone` (optional): Updated phone

5. **Delete Contact**
   - Tool name: `delete_contact`
   - Parameters:
     - `resource_name`: Contact resource name to delete

6. **Search Contacts**
   - Tool name: `search_contacts`
   - Parameters:
     - `query`: Search term to find in contacts
     - `max_results` (optional): Maximum number of results to return

7. **List Workspace Users**
   - Tool name: `list_workspace_users`
   - Parameters:
     - `query` (optional): Search term to find specific users
     - `max_results` (optional): Maximum number of results to return

8. **Search Directory**
   - Tool name: `search_directory`
   - Parameters:
     - `query`: Search term to find specific directory members
     - `max_results` (optional): Maximum number of results to return

9. **Get Other Contacts**
   - Tool name: `get_other_contacts`
   - Parameters:
     - `max_results` (optional): Maximum number of results to return

## Usage with MCP Clients

This server can be used with any MCP client. For example, with Claude for Desktop:

1. Start the server: `python main.py`
2. Set up the MCP connection in Claude for Desktop
3. Use any of the tools, for example:
   ```
   list_contacts(name_filter="John", max_results=10)
   ```
   ```
   search_contacts(query="john", max_results=5)
   ```

On first run, you'll need to authenticate through a browser window that opens automatically.

## Response Format

All responses are formatted as human-readable text instead of JSON, making them more suitable for consumption by language models. Each contact is formatted with details like:

```
Contact 1:
Name: John Doe
Email: john@example.com
Phone: +1 555-123-4567
ID: people/c123456789

Contact 2:
Name: Jane Smith
Email: jane@example.com
Phone: +1 555-987-6543
ID: people/c987654321

Found 2 contact(s)
```
