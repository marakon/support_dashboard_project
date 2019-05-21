import json

class JsonOperation:
    """ This class is processing json data into object readble for python.
        Requires Call() instance with choosen view.
        This is second called class."""
    def __init__(self, response):
        self.data = response
    
    def dump(self):
        """This function will generate a json file with given data."""
        with open('tickets.json', 'w') as json_file:  
            json.dump(self.data, json_file)
        return json_file
    
    def load(self):
        """This function generates data ready to send into different view of DataHandler() class."""
        loaded = json.loads(self.data.text)
        return loaded