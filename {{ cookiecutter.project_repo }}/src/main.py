import os
import json
import argparse
from utils.file_utils import load_input_data_from_json

from {{ cookiecutter.project_slug }}.processor import {{cookiecutter.__processor_class_name}}
def main(input_path=None):
    environment = os.getenv('APP_ENVIRONMENT', 'local')

    if environment == 'local':

        if input_path:
            input_data = load_input_data_from_json(input_path)
        else:
            input_data = load_input_data_from_json('data/processor_input_example.json')

    elif environment in ['integration', 'validation', 'production']:
        if not input_path:
            raise ValueError(f"No input path provided in the '{environment}' environment.")
        input_data = load_input_data_from_json(input_path)
    else:
        raise ValueError(f'Unrecognized environment: {environment}')

    processor = {{cookiecutter.__processor_class_name}}(input_data)

    result = processor.trigger()
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, help='Path to the input data', default=None)
    args = parser.parse_args()

    main(args.input_path)
