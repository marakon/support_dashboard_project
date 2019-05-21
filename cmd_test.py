#!/usr/bin/python3
from components import call_zendesk
from components import handler_zendesk
from components import json_zendesk

test_call = call_zendesk.Call().unassignedQueue()

test_response = json_zendesk.JsonOperation(test_call).load()

