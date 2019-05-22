#!/usr/bin/python3
from components import call_module
from components import handler_module
from components import json_module

import eel

eel.init("web")

test_call = call_module.Call()
unassigned_response = test_call.unassignedQueue

loaded_unassigned_response = json_module.JsonOperation(unassigned_response).load()
handle = handler_module.Handler()
handle.ticketCount = loaded_unassigned_response

@eel.expose
def ticket_count():
    return handle.ticketCount

eel.start("index.html", size=(600, 600))
