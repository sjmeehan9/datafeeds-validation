import sys
import os

# Get the directory of the current script
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (project_root)
project_root = os.path.dirname(current_script_path)

# Path to the scripts directory
scripts_path = os.path.join(project_root, 'scripts')

# Add the scripts directory to sys.path
sys.path.append(scripts_path)

# Now you can import main.py
import main

def test_data_validation():
    # Test that the data validation script runs without error
    # and returns the expected string
    assert main() == "Data validation completed successfully"