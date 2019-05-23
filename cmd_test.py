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
    (taken_bR, taken_nM, taken_mO, taken_hW, taken_aS, taken_wN, taken_mB) = taken_handle.ticketsPerAgent()
    return taken_bR, taken_nM, taken_mO, taken_hW, taken_aS, taken_wN, taken_mB

#==========================================================================================#
# Variables

(un_ticketCount, un_platinum, un_premium, unassigned_list) = unassigned()

# Premium and platinum together

(taken_bR, taken_nM, taken_mO, taken_hW, taken_aS, taken_wN, taken_mB) = teamTaken()
print(taken_bR)
print(taken_nM)
print(taken_mO)
print(taken_hW)
print(taken_aS)
print(taken_wN)
print(taken_mB)
#List of unassigned queue

#==========================================================================================#