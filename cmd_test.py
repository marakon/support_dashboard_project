#!/usr/bin/python3
from components import call_module as cz
from components import handler_module as hz
from components import json_module as jz

test_call = cz.Call()
aV = test_call.unassignedQueue
loaded = jz.JsonOperation(aV).load()
handle = hz.Handler()
(handle.tickets, handle.ticketCount, handle.premiumCount) = (loaded, loaded, loaded)
print(handle.premiumCount)
print(handle.viewTicketsCMD())

