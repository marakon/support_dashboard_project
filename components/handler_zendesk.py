#!/usr/bin/python3

class DataHandler:
    """ This class is storing data about tickets and handling it.
        Requires loaded data from JsonOpeartion().load() function.
        This is third called class."""
    def __init__(self, loaded):
        self._tickets = loaded['tickets'] # List of tickets stored in dict from the response
        self._count = loaded['count'] # Amount of tickets(objects in list)

    def viewTickets(self):
        """ This function is viewing the cases on the screen.
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
        tickets = []
        if self._count == 0:
            tickets.append(_clear)
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
                tickets.append(_ticket)
        return tickets