# GitHub Workflows

This directory contains GitHub Actions workflow files for automating tasks in this repository.

## Publish to PyPI

The `publish-to-pypi.yml` workflow automatically builds and publishes this package to PyPI when a new GitHub release is created.

### Setup Required

Before using this workflow, you need to:

1. Register an account on [PyPI](https://pypi.org/)
2. Generate an API token on PyPI:
   - Go to your PyPI account settings
   - Navigate to "API tokens"
   - Create a new token with "Entire account (all projects)" scope
3. Add the token as a GitHub repository secret:
   - Go to your GitHub repository settings
   - Navigate to "Secrets and variables" > "Actions"
   - Create a new repository secret named `PYPI_API_TOKEN` with your PyPI API token as the value

### Creating a Release

To publish a new version to PyPI:

1. Update the version number in `pyproject.toml`
2. Create a new release on GitHub:
   - Go to the "Releases" section of your repository
   - Click "Draft a new release"
   - Create a new tag in the format `v0.1.0`
   - Add a title and description for the release
   - Click "Publish release"

The workflow will then automatically build and publish the package to PyPI.
