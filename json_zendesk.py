import json
import call_zendesk

class JsonOperation:
    """ This class is processing json data into object readble for python.
        Requires Call() instance with choosen view.
        This is second called class."""
    def __init__(self, js):
        self.data = js
    
    def dump(self):
        """This function will generate a nice tree view for the given json. This is an object ready to view."""
        action = json.dumps(self.data.json())
        with open('views.txt', 'w') as json_file:  
            json.dump(action, json_file)
        return action
    
    def load(self):
        """This function generates data ready to send into different view of DataHandler() class."""
        action = json.loads(self.data.text)
        return action