
from jsonschema import validate, ValidationError
from schemas.output_schema import ProcessOutput,Metadata
import time
from datetime import datetime

class {{cookiecutter.__processor_class_name}}():

    def __init__(self, input_data):
        self.input_data = input_data


    def prepare_data(self):
        print("data_prepared")


    def predict(self, input_data):
        print("Output predicted")
        return "success"

    def trigger(self):
        start_time = time.time()
        print("Processor triggered")
        self.prepare_data()
        result = self.predict(self.input_data)
        end_time = time.time()
        duration_seconds = end_time - start_time
        output = ProcessOutput(
            status=result,
            datacube_url="http://geosysp3.blob.core.windows.net/analytic_datacube.zarr",
            metadata=Metadata(
                generated_timestamp=datetime.utcfromtimestamp(end_time).isoformat() + "Z" ,
                duration_seconds=duration_seconds,
                datacube_format="zarr"
            )
        )
        print("Processor output:", output)
        return output