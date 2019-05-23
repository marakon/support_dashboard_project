#!/usr/bin/python3
import datetime

class Calculate:
    """ This class is processing data about tickets.
        Requires loaded data from 'JsonOpeartion().load()' function.
        This is third called class."""
    def __init__(self):
        self._tickets = None # List of tickets stored in dict from the response
        self._views = None # All views in Zendesk
        self._count = 0 # Amount of tickets(objects in list)
        self._premium = 0
        self._platinum = 0

#==============================SETTERS============================GETTERS====================================#

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
    def premiumCount(self):
        """Returns premium count of the given view."""
        return self._premium

    @premiumCount.setter
    def premiumCount(self, loaded):
        for i in range(0, self._count):
            if self._tickets[i]['custom_fields'][15]['value'] == 'premium':
                self._premium += 1
    
    @property
    def platinumCount(self):
        """Returns platinum count of the given view."""
        return self._platinum

    @platinumCount.setter
    def platinumCount(self, loaded):
        for i in range(0, self._count):
            if self._tickets[i]['custom_fields'][15]['value'] == 'platinum':
                self._platinum += 1
    
    @property
    def ticketCount(self):
        """Returns tickets count of the given view."""
        return self._count

    @ticketCount.setter
    def ticketCount(self, loaded):
        self._count = loaded['count']

#============================================================================================================#
    @property
    def viewInCMD(self):
        """ This function is viewing the cases in the CMD.
            Requires data from JsonOparation().load() function."""
        if self._count == 0:
            print("Queue clear nice!")
        else:
            print("Current number of tickets: {0}".format(self._count))
            for i in range(0,self._count):
                print(self._tickets[i]['subject'], '\t',
                    self._tickets[i]['status'], '\t',
                    self._tickets[i]['custom_fields'][5]['value'], '\t',
                    self._tickets[i]['priority'], '\t',
                    self._tickets[i]['id'], '\t',
                    self._tickets[i]['created_at'])

    def detailedTickets(self):
        """ This function is preparing a new list of dict that will have only needed data.
            Requires data from JsonOparation().load() function."""
        _clear = "Queue clear nice!"
        _tickets = []
        if self._count == 0:
            _tickets.append(_clear)
        else:
            for i in range(0,self._count):
                _ticket = {
                    'subject':'',
                    'status':'',
                    'domain_name':'',
                    'priority':'',
                    'id':'',
                    'creation_date':''
                }
                _ticket['subject'] = self._tickets[i]['subject']
                _ticket['status'] = self._tickets[i]['status']
                _ticket['domain_name'] = self._tickets[i]['custom_fields'][5]['value']
                _ticket['priority'] = self._tickets[i]['priority']
                _ticket['id'] = self._tickets[i]['id']
                _ticket['creation_date'] = self._tickets[i]['created_at']
                _tickets.append(_ticket)
        return _tickets

    def allViews(self):
        """ This function is preparing a new list of dict that will have only needed data.
            Requires data from JsonOparation().load() function."""
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
    @property
    def unassignedView(self):
        """ This function is preparing a new list of dict that will have only needed data.
            Requires data from JsonOparation().load() function."""
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

    def jiraStatusView(self):
        """ This function is preparing a new list of dict that will have only needed data.
            Requires data from JsonOparation().load() function."""
        _tickets = []
        print(self._count)
        for i in range(self._count):
            if isinstance(self._tickets[i]['custom_fields'][24]['value'], str) and 'Waiting For Customer' in self._tickets[i]['custom_fields'][25]['value']:
                _ticket = {
                    'number':'',
                    'status':''
                }
                _ticket['number'] = self._tickets[i]['custom_fields'][24]['value']
                _ticket['status'] = self._tickets[i]['custom_fields'][25]['value']
                _tickets.append(_ticket)
        return _tickets
