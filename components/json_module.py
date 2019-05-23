#!/usr/bin/python3
import json as j

class JsonOperation:
    """ This class is processing json data into object readble for python.
        Requires Call() instance with choosen view.
        This is second called class."""
    def __init__(self, response):
        self._data = response

    def load(self):
        """This function generates data ready to send into different view of DataHandler() class."""
        return j.loads(self._data.text)