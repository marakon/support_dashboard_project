#!/usr/bin/python3
from components import call_module as cz
from components import handler_module as hz
from components import json_module as jz

call = cz.ZendeskCall()
handle = hz.Calculate()

poznanTickets = call.poznanTickets
jops = jz.JsonOperation(poznanTickets)
loaded = jops.load()
(handle.tickets, handle.ticketCount) = (loaded, loaded)
jira_status = handle.jiraStatusView()

