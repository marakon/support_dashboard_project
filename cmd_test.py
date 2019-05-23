#!/usr/bin/python3
from components import call_module
from components import handler_module
from components import json_module

def unassigned():
    unassigned_call = call_module.ZendeskCall()
    unassigned_handle = handler_module.Calculate()
    unassigned_raw = unassigned_call.unassignedQueue
    unassigned = json_module.JsonOperation(unassigned_raw)
    unassigned_loaded = unassigned.load()
    (unassigned_handle.tickets, unassigned_handle.ticketCount, unassigned_handle.platinumCount, unassigned_handle.premiumCount) = (unassigned_loaded, unassigned_loaded, unassigned_loaded, unassigned_loaded)
    unassigned_view = unassigned_handle.unassignedView
    return unassigned_handle.ticketCount, unassigned_handle.platinumCount, unassigned_handle.premiumCount, unassigned_view

def teamTaken():
    taken_call = call_module.ZendeskCall()
    taken_handle = handler_module.Calculate()
    taken_raw = taken_call.teamTaken
    taken = json_module.JsonOperation(taken_raw)
    taken_loaded = taken.load()
    (taken_handle.tickets, taken_handle.ticketCount) = (taken_loaded, taken_loaded)
    taken_view = taken_handle.viewInCMD
    return taken_handle.ticketCount, taken_view

#==========================================================================================#
# Variables

(un_ticketCount, un_platinum, un_premium, unassigned_list) = unassigned()

# Premium and platinum together

(taken_ticketCount, taken_list) = teamTaken()
#List of unassigned queue

#==========================================================================================#
# 'assignee_id'
# Bremesz = 374937979731
# Natalia = 360576935392
# MatO = 360561897751
# Hubert = 114101112231
# Ania = 370896464451
# Wojciech = 372919764412
# MatB = 114126187612