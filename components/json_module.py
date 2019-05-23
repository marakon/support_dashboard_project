#!/usr/bin/python3
import json as j

class JsonOperation:
    """ This class is processing json data into object readble for python.
        Requires Call() instance with choosen view.
        This is second called class."""
    def __init__(self, response):
        self._data = response

    def dump(self):
        """ This function will generate a json file with given data.
            Please call it after processing the data in DataHandler()"""
        with open('tickets.json', 'w') as json_file:  
            j.dump(self._data, json_file)
        return json_file

    def load(self):
        """This function generates data ready to send into different view of DataHandler() class."""
        return j.loads(self._data.text)