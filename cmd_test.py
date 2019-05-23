#!/usr/bin/python3
from components import call_module as cz
from components import handler_module as hz
from components import json_module as jz

call = cz.ZendeskCall()
handle = hz.Calculate()

<<<<<<< HEAD
poznanTickets = call.poznanTickets
jops = jz.JsonOperation(poznanTickets)
loaded = jops.load()
(handle.tickets, handle.ticketCount) = (loaded, loaded)
jira_status = handle.jiraStatusView()

=======
unassigned = call.unassignedQueue
jops.response = unassigned
loaded_unassigned = jops.load
(handle.tickets, handle.ticketCount) = (loaded_unassigned, loaded_unassigned)
print(handle.viewInCMD)
>>>>>>> a4e68dfc05fdc039947d21102aded41acb099d81
