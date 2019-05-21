import requests
import auth

class Call:
    """ This class is doing API calls to get data about certian views.
        This is first called class."""
    def __init__(self):
        self.view = 'https://egnyte.zendesk.com/api/v2/views'
        self.unassigned = self.view + '/461492/tickets.json'
        self.all = self.view + '/compact.json'
        self.open = self.view + '/461487/tickets.json'
        self.poznan = self.view + '/360053215891/tickets.json'

    def unassignedQueue(self):
        """API call to unassigned queue."""
        r = requests.get(self.unassigned, auth=auth.authorization_key)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Problem with the request. Exiting.')
            exit()
        return r

    def allViews(self):
        """API call to get all view in case of implementing new one. Best to send into JsonOperation().dump() function."""
        r = requests.get(self.all, auth=auth.authorization_key)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Problem with the request. Exiting.')
            exit()
        return r

    def myOpenTickets(self):
        """API call to my open tickets queue."""
        r = requests.get(self.open, auth=auth.authorization_key)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Problem with the request. Exiting.')
            exit()
        return r

    def poznanTickets(self):
        """API call to my open tickets queue."""
        r = requests.get(self.poznan, auth=auth.authorization_key)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Problem with the request. Exiting.')
            exit()
        return r