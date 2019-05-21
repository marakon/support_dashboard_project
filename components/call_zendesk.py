#!/usr/bin/python3
import requests

from data import auth
from data import views

class Call:
    """ This class is doing API calls to get data about certian views.
        This is first called class."""
    def __init__(self):
        self.unassigned = '{0}/{1}/tickets.json'.format(views.main_path, views.view_unassigned['id'])
        self.compact = '{0}/compact.json'.format(views.main_path)
        self.open = '{0}/{1}/tickets.json'.format(views.main_path, views.view_open['id'])
        self.poznan = '{0}/{1}/tickets.json'.format(views.main_path, views.view_poznan['id'])
        # Space below to add more views

    def unassignedQueue(self):
        """API call to unassigned queue."""
        response = requests.get(self.unassigned, auth=auth.authorization_key)
        if response.status_code != 200: print('Status:', response.status_code, 'Problem with the request. Exiting.')
        return response

    def allViews(self):
        """API call to get all view in case of implementing new one. Best to send into JsonOperation().dump() function."""
        response = requests.get(self.compact, auth=auth.authorization_key)
        if response.status_code != 200: print('Status:', response.status_code, 'Problem with the request. Exiting.')
        return response

    def myOpenTickets(self):
        """API call to my open tickets queue."""
        response = requests.get(self.open, auth=auth.authorization_key)
        if response.status_code != 200: print('Status:', response.status_code, 'Problem with the request. Exiting.')
        return response

    def poznanTickets(self):
        """API call to my open tickets queue."""
        response = requests.get(self.poznan, auth=auth.authorization_key)
        if response.status_code != 200: print('Status:', response.status_code, 'Problem with the request. Exiting.')
        return response
    
    # If you add new view in __init__ create a new function that will do call with its view.