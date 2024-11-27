#!/bin/bash
# Create the "models" directory if it doesn't exist
mkdir -p models

# Create and initialize "base.py" with a basic Python structure
echo "# base.py: Base classes and utilities for the project" > models/base.py
echo -e "\nclass Base:\n    pass" >> models/base.py

# Create and initialize "__init__.py" to make "models" a Python package
echo "# __init__.py: Initialize the models package" > models/__init__.py
