#!/usr/bin/python3

class DataHandler:
    """ This class is processing data about tickets.
        Requires loaded data from 'JsonOpeartion().load()' function.
        This is third called class."""
    def __init__(self, loaded):
        if 'tickets' in loaded:
            self._tickets = loaded['tickets'] # List of tickets stored in dict from the response
            self._count = loaded['count'] # Amount of tickets(objects in list)
        if 'views' in loaded:
            self._views = loaded['views'] # All views in Zendesk
            self._count = loaded['count'] # Amount of tickets(objects in list)

    def viewTicketsCMD(self):
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

    def ticketsToJson(self):
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
    
    def unassignedView(self):
        """ This function is preparing a new list of dict that will have only needed data.
            Requires data from JsonOparation().load() function."""
        _tickets = []
        for i in range(0,self._count):
            _ticket = {
                'subject':'',
                'domain_name':''
            }
            _ticket['subject'] = self._tickets[i]['subject']
            _ticket['domain_name'] = self._tickets[i]['custom_fields'][5]['value']
            _tickets.append(_ticket)
        return _tickets


# GETTERS FOR SINGLE VALUES
#============================================================================================================#
    def getPremiumCount(self):
        """Returns premium count of the given view."""
        _num_prem = 0
        for i in range(0, self._count):
            if self._tickets[i]['custom_fields'][15]['value'] == 'premium':
                num_prem += 1
        return _num_prem

    def getTicketCount(self):
        """Returns tickets count of the given view."""
        return self._count