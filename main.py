#!/usr/bin/python3
from components import call_module
from components import handler_module
from components import json_module

import eel

# eel.init("web")

def unassigned():
    unassigned_call = call_module.ZendeskCall()
    unassigned_handle = handler_module.Calculate()
    unassigned_raw = unassigned_call.unassignedQueue
    unassigned = json_module.JsonOperation(unassigned_raw)
    unassigned_loaded = unassigned.load()
    (unassigned_handle.ticketCount, unassigned_handle.platinumCount, unassigned_handle.premiumCount, unassigned_handle.tickets) = (unassigned_loaded, unassigned_loaded, unassigned_loaded, unassigned_loaded)
    unassigned_view = unassigned_handle.unassignedView()
    return unassigned_handle.ticketCount, unassigned_handle.platinumCount, unassigned_handle.premiumCount, unassigned_view

#==========================================================================================#
# Variables

(un_ticketsCount, un_platinum, un_premium, unassigned_list) = unassigned()

# Premium and platinum together
prem_and_plat = un_premium + un_platinum

#List of unassigned queue

#==========================================================================================#


# @eel.expose
# def ticket_count():
#     return un_ticketsCount

# eel.start("index.html", size=(1280, 720))
