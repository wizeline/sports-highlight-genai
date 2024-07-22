#!/bin/bash

# Activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# Run tests with pytest
pytest src/tests

# Deactivate the virtual environment
deactivate