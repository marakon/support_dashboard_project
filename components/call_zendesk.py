#!/usr/bin/python3
import requests

from components.files import views as v
from components.files.auth import key

class Call:
    """ This class is doing API calls to get data about certian views.
        This is first called class."""
    def __init__(self):
        self._unassigned = '{0}/{1}/tickets.json'.format(v.main_path, v.view_unassigned['id'])
        self._compact = '{0}/compact.json'.format(v.main_path)
        self._open = '{0}/{1}/tickets.json'.format(v.main_path, v.view_open['id'])
        self._poznan = '{0}/{1}/tickets.json'.format(v.main_path, v.view_poznan['id'])
        # Space below to add more views

    def unassignedQueue(self):
        """API call to unassigned queue."""
        response = requests.get(self._unassigned, auth=key)
        if response.status_code != 200: print('Status:', response.status_code, 'Problem with the request. Exiting.')
        return response

    def allViews(self):
        """API call to get all view in case of implementing new one. Best to send into JsonOperation().dump() function."""
        response = requests.get(self._compact, auth=key)
        if response.status_code != 200: print('Status:', response.status_code, 'Problem with the request. Exiting.')
        return response

    def myOpenTickets(self):
        """API call to my open tickets queue."""
        response = requests.get(self._open, auth=key)
        if response.status_code != 200: print('Status:', response.status_code, 'Problem with the request. Exiting.')
        return response

    def poznanTickets(self):
        """API call to my open tickets queue."""
        response = requests.get(self._poznan, auth=key)
        if response.status_code != 200: print('Status:', response.status_code, 'Problem with the request. Exiting.')
        return response
    
    # If you add new view in __init__ create a new function that will do call with its view.