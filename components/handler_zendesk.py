#!/usr/bin/python3
class DataHandler:
    """ This class is storing data about tickets and handling it.
        Requires loaded data from JsonOpeartion().load() function.
        This is third called class."""
    def __init__(self, loaded):
        self.tickets = loaded['tickets'] # List of tickets stored in dict from the response
        self.count = loaded['count'] # Amount of tickets(objects in list)

    def viewTickets(self):
        """ This function is viewing the cases on the screen.
            Requires data from JsonOparation().load() function."""
        if self.count == 0:
            print("Queue clear nice!")
        else:
            print("Current number of tickets:", self.count)
            for i in range(0,self.count):
                print(self.tickets[i]['subject'], '\t',
                    self.tickets[i]['status'], '\t',
                    self.tickets[i]['custom_fields'][5]['value'], '\t',
                    self.tickets[i]['priority'], '\t',
                    self.tickets[i]['id'], '\t',
                    self.tickets[i]['created_at'])

    def ticketsToJson(self):
        """ This function is preparing a new list of dict that will have only needed data.
            Requires data from JsonOparation().load() function."""
        tickets = []
        if self.count == 0:
            print("Queue clear nice!")
        else:
            print("Current number of tickets:", self.count)
            for i in range(0,self.count):
                ticket = {
                    'subject':'',
                    'status':'',
                    'domain_name':'',
                    'priority':'',
                    'id':'',
                    'creation_date':''
                }
                ticket['subject'] = self.tickets[i]['subject']
                ticket['status'] = self.tickets[i]['status']
                ticket['domain_name'] = self.tickets[i]['custom_fields'][5]['value']
                ticket['priority'] = self.tickets[i]['priority']
                ticket['id'] = self.tickets[i]['id']
                ticket['creation_date'] = self.tickets[i]['created_at']
                tickets.append(ticket)
        return tickets