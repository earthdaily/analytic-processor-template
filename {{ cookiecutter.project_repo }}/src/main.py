import os
import json
from utils.file_utils import load_input_data

from {{ cookiecutter.project_slug }}.processor import {{cookiecutter.__processor_class_name}}
def main():
    input_data = load_input_data()
    processor = {{cookiecutter.__processor_class_name}}(input_data)

    result = processor.trigger()
    return result

if __name__ == '__main__' :
    main()
