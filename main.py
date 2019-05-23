#!/usr/bin/python3
from components import call_module
from components import handler_module
from components import json_module

import eel

eel.init("web")

unassigned_call = call_module.ZendeskCall()
unassigned_handle = handler_module.Calculate()
unassigned_raw = unassigned_call.unassignedQueue
unassigned = json_module.JsonOperation(unassigned_raw)
unassigned_loaded = unassigned.load()
(unassigned_handle.tickets, unassigned_handle.ticketCount, unassigned_handle.platinumCount, unassigned_handle.premiumCount) = (unassigned_loaded, unassigned_loaded, unassigned_loaded, unassigned_loaded)

#==========================================================================================#
# Variables

# Number of premium cases
premium = unassigned_handle.premiumCount

# Number of platinum cases
platinum = unassigned_handle.platinumCount

# Premium and platinum together
prem_and_plat = premium + platinum

# List of unassigned queue
unassignedView = unassigned_handle.unassignedView()

# Number of tickets in unassigned
ticketsCount = unassigned_handle.ticketCount
#==========================================================================================#


@eel.expose
def ticket_count():
    return unassignedView

eel.start("index.html", size=(600, 600))
