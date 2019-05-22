#!/usr/bin/python3
from components import call_zendesk as cz
from components import handler_zendesk as hz
from components import json_zendesk as jz

test_call = cz.Call()
aV = test_call.unassignedQueue()
loaded = jz.JsonOperation(aV).load()
hz.DataHandler(loaded).priority()