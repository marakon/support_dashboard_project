import requests
import auth
import views

class Call:
    """ This class is doing API calls to get data about certian views.
        This is first called class."""
    def __init__(self):
        self.unassigned = '{0}/{1}/tickets.json'.format(views.main_path, views.view_unassigned['id'])
        self.compact = '{0}/compact.json'.format(views.main_path)
        self.open = '{0}/{1}/tickets.json'.format(views.main_path, views.view_open['id'])
        self.poznan = '{0}/{1}/tickets.json'.format(views.main_path, views.view_poznan['id'])

    def unassignedQueue(self):
        """API call to unassigned queue."""
        r = requests.get(self.unassigned, auth=auth.authorization_key)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Problem with the request. Exiting.')
            exit()
        return r

    def allViews(self):
        """API call to get all view in case of implementing new one. Best to send into JsonOperation().dump() function."""
        r = requests.get(self.compact, auth=auth.authorization_key)
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