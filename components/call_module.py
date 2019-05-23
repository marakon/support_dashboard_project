#!/usr/bin/python3
import requests
from jira import JIRA

from components.files import views as v
from components.files import auth

class ZendeskCall:
    """ This class is doing API calls to get data about certian views.
        This is first called class."""
    def __init__(self):
        self._unassigned = '{0}/{1}/tickets.json'.format(v.main_path, v.view_unassigned['id'])
        self._compact = '{0}/compact.json'.format(v.main_path)
        self._open = '{0}/{1}/tickets.json'.format(v.main_path, v.view_open['id'])
        self._poznan = '{0}/{1}/tickets.json'.format(v.main_path, v.view_poznan['id'])
        self._team_taken = '{0}/{1}/tickets.json'.format(v.main_path, v.view_team_taken['id'])
        self._team_solved = '{0}/{1}/tickets.json'.format(v.main_path, v.view_team_solved['id'])
        # Space below to add more views

    @property
    def unassignedQueue(self):
        """API call to unassigned queue."""
        response = requests.get(self._unassigned, auth=auth.key)
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
        return response

    @property
    def allViews(self):
        """API call to get all view in case of implementing new one. Best to send into JsonOperation().dump() function."""
        response = requests.get(self._compact, auth=auth.key)
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
        return response

    @property
    def myOpenTickets(self):
        """API call to my open tickets queue."""
        response = requests.get(self._open, auth=auth.key)
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
        return response

    @property
    def poznanTickets(self):
        """API call to my open tickets queue."""
        response = requests.get(self._poznan, auth=auth.key)
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
        return response
    
    # If you add new view in __init__ create a new function that will do call with its view.

    @property
    def teamTaken(self):
        """API call to my open tickets queue."""
        response = requests.get(self._team_taken, auth=auth.key)
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
        return response

    @property
    def teamSolved(self):
        """API call to my open tickets queue."""
        response = requests.get(self._team_solved, auth=auth.key)
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
        return response


# class JiraCall:

#     jira = JIRA('https://jira.egnyte-it.com', auth=auth.jira_key)

#     issue = jira.issue('ESC-17609')
#     print (issue.fields.project.key)
#     print (issue.fields.issuetype.name)
#     print (issue.fields.reporter.displayName)