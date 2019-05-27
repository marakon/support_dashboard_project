#!/usr/bin/python3
import datetime

class Calculate:
    """ This class is processing data about tickets."""
    def __init__(self):
        self._tickets = None
        self._views = None
        self._count = 0
        self._premium = 0
        self._platinum = 0

#======================SETTERS====================GETTERS========================#

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
            if self._tickets[i]['custom_fields'][15]['value'] is 'premium':
                self._premium += 1
    
    @property
    def platinum_count(self):
        """Returns platinum count of the given view."""
        return self._platinum

    @platinum_count.setter
    def platinum_count(self, loaded):
        for i in range(0, self._count):
            if self._tickets[i]['custom_fields'][15]['value'] is 'platinum':
                self._platinum += 1
    
    @property
    def ticket_count(self):
        """Returns tickets count of the given view."""
        return self._count

    @ticket_count.setter
    def ticket_count(self, loaded):
        self._count = loaded['count']

#============================================================================================================#
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
        for i in range(0,self._count):
            _view = {
                'id':'',
                'title':'',
                'active':'',
            }
            _view['id'] = self._views[i]['id']
            _view['title'] = self._views[i]['title']
            _view['active'] = self._views[i]['active']
            _views.append(_view)
        return _views
        
    def unassigned_view(self):
        """ This function is preparing a new list of dict that will have:
            ID, subject, domain_name, plan, priority, created date."""
        _tickets = []
        for i in range(0,self._count):
            _ticket = {
                'id': '',
                'subject':'',
                'domain_name':'',
                'plan':'',
                'priority':'',
                'created_at':''
            }
            _ticket['id'] = self._tickets[i]['id']
            _ticket['subject'] = self._tickets[i]['subject']
            _ticket['domain_name'] = self._tickets[i]['custom_fields'][5]['value']
            _ticket['plan'] = self._tickets[i]['custom_fields'][15]['value']
            _ticket['priority'] = self._tickets[i]['priority']
            _ticket['created_at'] = self._tickets[i]['created_at']
            _tickets.append(_ticket)
        return _tickets

    def jira_status_view(self):
        """ This function is preparing a new list of dict that will
            have details about JIRA tickets(number and status)."""
        _tickets = []
        for i in range(self._count):
            if (isinstance(self._tickets[i]['custom_fields'][24]['value'], str) and
            'Waiting For Customer' in self._tickets[i]['custom_fields'][25]['value']):
            # Field needs to be str and Waiting For Customers state
                _ticket = {
                    'number':'',
                    'status':''
                }
                _ticket['number'] = self._tickets[i]['custom_fields'][24]['value']
                _ticket['status'] = self._tickets[i]['custom_fields'][25]['value']
                _tickets.append(_ticket)
        return _tickets
    
    def jira_not_updated(self):
        """ This function is preparing a new list of dict that will
            have details about JIRA tickets(number and status)."""
        jira_tickets = []
        for i in range(self._count):
            if isinstance(self._tickets[i]['custom_fields'][24]['value'], str):
                jira_tickets.append(self._tickets[i]['custom_fields'][24]['value'])
        return jira_tickets

    def tickets_per_agent(self):
        """ This function is preparing list with numbers of taken/solved cases by agent."""
        (_mosinski, _bremesz, _nmagon, _hwozniak, _asito, _wniekrasz, _mbukowian) = (0, 0, 0, 0, 0, 0, 0)
        agents_list = [
            _mosinski,
            _bremesz,
            _nmagon,
            _hwozniak,
            _asito,
            _wniekrasz,
            _mbukowian
            ]
        agents_ids = {
            0: 360561897751,
            1: 374937979731,
            2: 360576935392,
            3: 114101112231,
            4: 370896464451,
            5: 372919764412,
            6: 114126187612
            }
        for i in range (self._count):
            for list_id, agent_id in agents_ids.items():
                if agent_id == self._tickets[i]['assignee_id']:
                    agents_list[list_id] += 1
        return agents_list
