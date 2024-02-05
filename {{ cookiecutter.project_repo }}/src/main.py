import os
import argparse
import json
from dotenv import load_dotenv
from utils.file_utils import load_input_data, save_output_file

from {{ cookiecutter.project_slug }}.processor import {{cookiecutter.__processor_class_name}}
def main(input_path=None, input_data=None):
    load_dotenv()
    environment = os.getenv('APP_ENVIRONMENT', 'local')
    if environment == 'local':
        data = load_input_data(os.getenv('INPUT_JSON_PATH'))

    elif environment in ['validation', 'production']:
        if input_path is not None and os.path.isfile(input_path):
            data = load_input_data(input_path)
        elif input_data is not None:
            try:
                data = json.loads(input_data)
            except json.JSONDecodeError:
                raise ValueError("Input data is not a valid JSON string")
        else:
            raise ValueError("No valid input provided in the '{environment}' environment.")
    else:
        raise ValueError(f'Unrecognized environment: {environment}')

    processor = {{cookiecutter.__processor_class_name}}(data)
    result = processor.trigger()
    if environment in ['validation', 'production']:
        save_output_file(result)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, help='Path to the input data', default=None)
    parser.add_argument('--input_data', type=str, help='input data', default=None)

    args = parser.parse_args()

    main(args.input_path,args.input_data)
