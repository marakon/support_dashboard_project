#!/usr/bin/python3
from components import call_module
from components import handler_module
from components import json_module

import eel

eel.init("web")

call = call_module.ZendeskCall()
jops = json_module.JsonOperation()
handle = handler_module.Calculate()

unassigned = call.unassignedQueue
print(unassigned)
jops.response = unassigned
loaded_unassigned = jops.load
(handle.tickets, handle.ticketCount) = (loaded_unassigned, loaded_unassigned)


@eel.expose
def ticket_count():
    return handle.unassignedView

eel.start("index.html", size=(600, 600))
