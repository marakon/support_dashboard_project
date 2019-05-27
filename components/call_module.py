#!/usr/bin/python3
import requests as r
import json as j
import dateutil.parser as du
from jira import JIRA
from datetime import datetime as dt, timezone as tz

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
    def unassigned_queue(self):
        """API call to unassigned queue."""
        resp = r.get(self._unassigned, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)

    @property
    def all_views(self):
        """API call to get all view in case of implementing new one. Best to send into JsonOperation().dump() function."""
        resp = r.get(self._compact, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)

    @property
    def my_open_tickets(self):
        """API call to my open tickets queue."""
        resp = r.get(self._open, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)

    @property
    def poznan_tickets(self):
        """API call to my open tickets queue."""
        resp = r.get(self._poznan, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)
    
    # If you add new view in __init__ create a new function that will do call with its view.

    @property
    def team_taken(self):
        """API call to my open tickets queue."""
        resp = r.get(self._team_taken, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)

    @property
    def team_solved(self):
        """API call to my open tickets queue."""
        resp = r.get(self._team_solved, auth=a.key)
        if resp.status_code != 200:
            print('Status:', resp.status_code, 'Problem with the request. Exiting.')
            exit()
        return j.loads(resp.text)


class JiraCall:

    def __init__(self):
        self._call = JIRA('https://jira.egnyte-it.com', auth=a.jira_key)
        self._id = None

    def view_jira_details(self):
        issue = self._call.issue('ESC-17609')
        now = dt.now(tz.utc)
        time = du.parse(issue.fields.worklog.worklogs[0].updated)
        print (issue.fields.issuetype.name)
        print (issue.fields.reporter.displayName)
        delta = now - time
        print (delta.days)