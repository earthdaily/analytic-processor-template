import json
from schemas.input_schema import input_Model

def load_input_data(input_data_path):
    """Load and return the input data from JSON file."""
    with open(input_data_path, 'r') as file:
        input_data = json.load(file)
    return input_data

def validate_input_model(input_data_path):
    try:
        input_json = load_input_data(input_data_path)
        input_model = input_Model(**input_json)
        print(input_model)
        return input_model

    except Exception as e:
        print(f"An error occurred: {e}")

