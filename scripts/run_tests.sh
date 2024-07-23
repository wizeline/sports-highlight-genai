#!/bin/bash

# Create a virtual environment if it does not exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run tests with pytest
pytest src/tests

# Deactivate the virtual environment
deactivate
