#!/usr/bin/python3
from components import call_module as cz
from components import handler_module as hz
from components import json_module as jz

call = cz.ZendeskCall()
jops = jz.JsonOperation()
handle = hz.Calculate()

unassigned = call.unassignedQueue
jops.response = unassigned
loaded_unassigned = jops.load
(handle.tickets, handle.ticketCount) = (loaded_unassigned, loaded_unassigned)
print(handle.viewInCMD)
