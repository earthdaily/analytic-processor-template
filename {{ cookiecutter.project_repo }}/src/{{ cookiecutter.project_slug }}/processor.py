
import time
from datetime import datetime
from utils.file_utils import validate_data

class {{cookiecutter.__processor_class_name}}():

    def __init__(self, input_data):
        validate_data(input_data, 'input')
        self.input_data = input_data
    

    def prepare_data(self):
        print("data_prepared")


    def predict(self, input_data):
        print("Output predicted")
        return "Completed"

    def trigger(self):
        start_time = time.time()
        print("Processor triggered")
        self.prepare_data()
        result = self.predict(self.input_data)
        output_data = {
            "Metadata": {
                "processId": "123",
                "processName": "SeasonAnalysis",
                "outputFormat": "zarr"
            },
            "ProcessOutput": {
                "status": result,
                "outputPath": "http://geosysp3.blob.core.windows.net/example_analytic_datacube.zarr",
                "error": ""
            }
        }

        validate_data(output_data, 'output')

        print("Processor output:", output_data)
        return output_data