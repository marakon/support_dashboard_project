#!/usr/bin/python3
from components import call_module
from components import handler_module
from components import json_module

call = call_module.ZendeskCall()
allView = call.allViews
json_file = json_module.JsonOperation(allView)
loaded = json_file.load()
calc = handler_module.Calculate()
calc.ticketCount = loaded
calc.tickets = loaded
print(calc.allViews())

