import json
from schemas.input_schema import InputModel
from schemas.output_schema import OutputModel
def load_input_data(input_data_path):
    """Load and return the input data from JSON file."""
    with open(input_data_path, 'r') as file:
        input_data = json.load(file)
    return input_data

def validate_data(data, data_type):
    try:
        if data_type == 'input':
            InputModel(**data)
        elif data_type == 'output':
            OutputModel(**data)
        else:
            raise ValueError("Invalid data_type. Must be 'input' or 'output'.")
    except PydanticValidationError as e:
        print(f"Pydantic validation error: {e}")
        raise
