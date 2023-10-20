import json
import os

def load_input_schema():
    """Load and return the input schema from the JSON file."""
    base_dir = os.path.dirname(__file__)
    schema_path = os.path.join(base_dir, '..', 'schemas', 'input_schema.json')

    with open(schema_path, 'r') as file:
        schema = json.load(file)
    return schema

def load_input_data():
    """Load and return the input data from the JSON file."""
    base_dir = os.path.dirname(__file__)
    input_data_path = os.path.join(base_dir, '..', 'data', 'processor_input1.json')

    with open(input_data_path, 'r') as file:
        input_data_path = json.load(file)
    return input_data_path