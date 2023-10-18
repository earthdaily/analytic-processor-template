

class {{cookiecutter.__processor_class_name}}():
    def __init__(self, parameters, context):
        self.params = parameters
        self.context = context

    def prepare_data(self):
        ### PRE PROCCESSING
        print("data_prepareed")


    def predict(self, params, context):
        # Detect harvest
        print("predicted")
        return "OK"

    def trigger(self):
        print("triggered")
        self.prepare_data()
        result = self.predict(self.params, self.context)
        return result