
from jsonschema import validate, ValidationError
from utils.file_utils import load_input_schema

class {{cookiecutter.__processor_class_name}}():

    def __init__(self, input_data):
        self.input_data = input_data
        self.schema = load_input_schema()
        self.validate_input()  # If validation fails, an exception will be raised immediately.
    def validate_input(self):
        """Validate the input data against the input schema."""
        try:
            validate(instance=self.input_data, schema=self.schema)
        except ValidationError as e:
            print(f"Input validation error: {e.message}")
            raise


    def prepare_data(self):
        ### PRE PROCCESSING
        print("data_prepareed")


    def predict(self, input_data):
        print("predicted")
        return "OK"

    def trigger(self):
        print("triggered")
        self.prepare_data()
        result = self.predict(self.input_data)
        return result