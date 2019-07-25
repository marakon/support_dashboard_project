#!/usr/bin/python3
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from components.files import blueprints as b
import re

class Calculate:
    """ This class is processing data about tickets."""
    def __init__(self):
        self._tickets = None
        self._views = None
        self._count = 0
        self._premium = 0
        self._platinum = 0
        self._transfer = 0

#======================SETTERS====================GETTERS===================#

    @property
    def tickets(self):
        return self._tickets

    @tickets.setter
    def tickets(self, loaded):
        if 'tickets' in loaded:
            self._tickets = loaded['tickets']
        if 'views' in loaded:
            self._views = loaded['views']

    @property
    def premium_count(self):
        """Returns premium count of the given view."""
        return self._premium

    @premium_count.setter
    def premium_count(self, loaded):
        for i in range(0, self._count):
            if self._tickets[i]['custom_fields'][15]['value'] == 'premium':
                self._premium += 1

    @property
    def platinum_count(self):
        """Returns platinum count of the given view."""
        return self._platinum

    @platinum_count.setter
    def platinum_count(self, loaded):
        for i in range(0, self._count):
            if self._tickets[i]['custom_fields'][15]['value'] == 'platinum':
                self._platinum += 1

    @property
    def ticket_count(self):
        """Returns tickets count of the given view."""
        return self._count

    @ticket_count.setter
    def ticket_count(self, loaded):
        self._count = loaded['count']
    
    @property
    def transfer_count(self):
        return self._transfer

    @transfer_count.setter 
    def  transfer_count(self, loaded):
        for i in range(0, self._count):
            if self._tickets[i]['group_id'] == 360002974692:
                self._transfer += 1

#===========================================================================#
    @property
    def view_in_cmd(self):
        """ This function is viewing the cases in the CMD.
            For testing the code."""
        if self._count is 0:
            print("Queue clear nice!")
        else:
            print("Current number of tickets: {0}".format(self._count))
            for i in range(0,self._count):
                print(self._tickets[i])

    def all_views(self):
        """ This function is preparing a new list of dict that will have
            ID, title and if the ticket is active."""
        _views = []
        for view_number in range(self._count):
            _view = b.view
            _view['id'] = self._views[view_number]['id']
            _view['title'] = self._views[view_number]['title']
            _view['active'] = self._views[view_number]['active']
            _views.append(_view)
        return _views
        
    def unassigned_view(self):
        """ This function is preparing a new list of dict that will have:
            ID, domain_name, plan, created date."""
        _tickets = []
        for case_number in range(self._count):
            _ticket = []
            _ticket.append(self._tickets[case_number]['id'])
            _ticket.append(self.name_check(self._tickets[case_number]['custom_fields'][5]['value']))
            _ticket.append(self.name_check(self._tickets[case_number]['custom_fields'][15]['value']))
            _ticket.append(self.calculate_delta_time(case_number))
            _tickets.append(_ticket)
        return _tickets

    def not_answered_view(self):
        """ This function is preparing a new list of dict that will have:
            ID, domain_name, plan, created date."""
        _tickets = []
        for case_number in range(self._count):
            _ticket = []
            _ticket.append(self._tickets[case_number]['id'])
            _ticket.append(self.name_check(self._tickets[case_number]['custom_fields'][5]['value']))
            _ticket.append(self.assignee())
            _tickets.append(_ticket)
        return _tickets

    def jira_status_view(self):
        """ This function is preparing a new list of dict that will
            have details about JIRA tickets(number and status)."""
        _tickets = []
        for case_number in range(self._count):
            (jira_number, jira_status) = (self._tickets[case_number]['custom_fields'][24]['value'],
                                          self._tickets[case_number]['custom_fields'][25]['value'])
            if (isinstance(jira_number, str) and 'Waiting For Customer' in jira_status):
                jira_ticket = b.jira_ticket
                jira_ticket['number'] = jira_number
                jira_ticket['status'] = jira_status
                _tickets.append(jira_ticket)
        return _tickets

    def jira_not_updated(self):
        #TODO:
        # Check if ticket was updated lass than 3 days ago
        """ This function is preparing a new list of dict that will
            have details about JIRA tickets(number and status)."""
        jira_tickets = []
        for case_number in range(self._count):
            jira_number = self._tickets[case_number]['custom_fields'][24]['value']
            if isinstance(jira_number, str):
                jira_tickets.append(jira_number)
        return jira_tickets

    def tickets_per_agent(self):
        """ This function is preparing list with numbers of taken/solved cases by agent."""
        (_mosinski, _bremesz, _hgautam,
         _wniekrasz, _jburda) = (0, 0, 0, 0, 0)
        agents_list = [
            _mosinski,
            _bremesz,
            _hgautam,
            _wniekrasz,
            _jburda
            ]
        agents_ids = b.agents_ids
        for case_number in range(self._count):
            for list_id, agent_id in agents_ids.items():
                if agent_id == self._tickets[case_number]['assignee_id']:
                    agents_list[list_id] += 1
        return agents_list

    def calculate_delta_time(self, case_number):
        created_time = datetime.strptime(self._tickets[case_number]['created_at'], '%Y-%m-%dT%H:%M:%SZ').time()
        now = datetime.time(datetime.utcnow().replace(microsecond=0))
        difference_delta = timedelta(hours=now.hour,
                                     minutes=now.minute,
                                     seconds=now.second)\
                         - timedelta(hours=created_time.hour,
                                     minutes=created_time.minute,
                                     seconds=created_time.second)
        alert = str(difference_delta.seconds//60%60) + ' min ago'
        return alert
        
    def name_check(self, item):
        if item == None:
            item = 'Not defined'
        if ',' in item:
            comma = item.find(',')
            item = item[:comma]
        return item
    
    def assignee(self):
        agents_list = [
            "MateuszO",
            "BartoszR",
            "HarshG",
            "WojciechN",
            "JakubB"
            ]
        agents_ids = b.agents_ids
        for case_number in range(self._count):
            for list_id, agent_id in agents_ids.items():
                if agent_id == self._tickets[case_number]['assignee_id']:
                    agent = agents_list[list_id]
        return agent