import os
import argparse
from dotenv import load_dotenv
from utils.file_utils import load_input_data

from {{ cookiecutter.project_slug }}.processor import {{cookiecutter.__processor_class_name}}
def main(input_path=None):
    load_dotenv()
    environment = os.getenv('APP_ENVIRONMENT', 'local')
    if environment == 'local':
        input_data = load_input_data(os.getenv('INPUT_JSON_PATH'))

    elif environment in ['integration', 'validation', 'production']:
        if not input_path:
            raise ValueError(f"No input path provided in the '{environment}' environment.")
        input_data = load_input_data(input_path)
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
