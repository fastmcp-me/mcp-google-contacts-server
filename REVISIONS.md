# REVISIONS.md - MCP Google Contacts Server

This document details the modifications applied to the `rayanzaki/mcp-google-contacts-server` repository to enable successful installation and operation as a Python package.

## Version 0.1.1 (Proposed)

### Fixes:

1.  **Installation Failure (`pip install .`)**: The original `pyproject.toml` expected the package directory to be `mcp_google_contacts_server`, but the source code was located in `src/`. This caused the `pip install .` command to fail with an `error: package directory 'mcp_google_contacts_server' does not exist`.
    *   **Solution**: Renamed the `src/` directory to `mcp_google_contacts_server/`.

2.  **Module Not Found Errors (`ModuleNotFoundError`)**: After initial installation (post-directory rename), running the `mcp-google-contacts` entry point resulted in `ModuleNotFoundError` for internal modules (e.g., `tools`, `config`, `google_contacts_service`, `formatters`). This was due to relative imports being used where absolute imports (relative to the installed package) were required.
    *   **Solution**: Updated all relative import statements in `main.py`, `tools.py`, and `google_contacts_service.py` to use absolute imports (e.g., `from mcp_google_contacts_server.tools import ...`).

### Updated Files:

*   `mcp_google_contacts_server/main.py`
*   `mcp_google_contacts_server/tools.py`
*   `mcp_google_contacts_server/google_contacts_service.py`
*   `pyproject.toml` (version bump)
*   `README.md` (installation instructions updated)

### Installation Steps (Corrected):

To install this package from source after cloning the repository:

1.  **Rename the source directory:**
    ```bash
    mv src mcp_google_contacts_server
    ```
2.  **Install the package:**
    ```bash
    pip install .
    ```

These changes ensure that the package can be installed correctly and its entry point script functions as expected.
