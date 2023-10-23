import json
import os

def load_input_schema():
    """Load and return the input schema from JSON file."""
    base_dir = os.path.dirname(__file__)
    schema_path = os.path.join(base_dir, '..', 'schemas', 'input_schema.json')

    with open(schema_path, 'r') as file:
        schema = json.load(file)
    return schema

def load_input_data_from_json(input_data_path):
    """Load and return the input data from JSON file."""
    # base_dir = os.path.dirname(__file__)
    # input_data_path = os.path.join(base_dir, '..', 'data', file_name)

    with open(input_data_path, 'r') as file:
        input_data = json.load(file)
    return input_data