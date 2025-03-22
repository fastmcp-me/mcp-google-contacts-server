from setuptools import setup, find_packages

setup(
    name="mcp-google-contacts-server",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # ...existing dependencies...
    ],
    entry_points={
        "console_scripts": [
            # ...existing entry points...
        ]
    },
)
