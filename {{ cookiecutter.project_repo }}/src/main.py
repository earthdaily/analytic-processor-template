import os
import json
# from api import api
# app= api.app
from {{ cookiecutter.project_slug }}.processor import {{cookiecutter.__processor_class_name}}
def main():
    # return app
    parameters = {}  # Add necessary parameters
    context = {}  # Add necessary context
    processor = {{cookiecutter.__processor_class_name}}(parameters, context)
    result = processor.trigger()
    return result

if __name__ == '__main__' :
    main()
