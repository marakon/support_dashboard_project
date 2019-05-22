#!/usr/bin/python3
from components import call_zendesk
from components import handler_zendesk
from components import json_zendesk

test_call = call_zendesk.Call()
uAQ = test_call.unassignedQueue()

test_response = json_zendesk.JsonOperation(uAQ).load()

print(handler_zendesk.DataHandler(test_response).viewTickets())