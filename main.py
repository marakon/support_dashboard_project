#!/usr/bin/python3
from components import call_zendesk
from components import handler_zendesk
from components import json_zendesk

import eel

eel.init("web")

test_call = call_zendesk.Call().unassignedQueue()

test_response = json_zendesk.JsonOperation(test_call).load()

@eel.expose
def ticket_count():
    return handler_zendesk.DataHandler(test_response).count()

eel.start("index.html", size=(600, 600))
