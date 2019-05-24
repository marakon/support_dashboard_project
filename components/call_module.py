#!/usr/bin/python3
import requests as r
import json as j
from jira import JIRA

from components.files import views as v
from components.files import auth as a

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
        resp = r.get(self._unassigned, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)

    @property
    def allViews(self):
        """API call to get all view in case of implementing new one. Best to send into JsonOperation().dump() function."""
        resp = r.get(self._compact, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)

    @property
    def myOpenTickets(self):
        """API call to my open tickets queue."""
        resp = r.get(self._open, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)

    @property
    def poznanTickets(self):
        """API call to my open tickets queue."""
        resp = r.get(self._poznan, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)
    
    # If you add new view in __init__ create a new function that will do call with its view.

    @property
    def teamTaken(self):
        """API call to my open tickets queue."""
        resp = r.get(self._team_taken, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)

    @property
    def teamSolved(self):
        """API call to my open tickets queue."""
        resp = r.get(self._team_solved, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)


# class JiraCall:

#     jira = JIRA('https://jira.egnyte-it.com', auth=auth.jira_key)

#     issue = jira.issue('ESC-17609')
#     print (issue.fields.project.key)
#     print (issue.fields.issuetype.name)
#     print (issue.fields.reporter.displayName)