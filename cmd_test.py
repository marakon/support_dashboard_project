#!/usr/bin/python3
from components import call_module
from components import handler_module

def unassigned():
    unassigned_call = call_module.ZendeskCall()
    unassigned_handle = handler_module.Calculate()
    unassigned_raw = unassigned_call.unassignedQueue
    (unassigned_handle.tickets, unassigned_handle.ticketCount, unassigned_handle.platinumCount, unassigned_handle.premiumCount) = (unassigned_raw, unassigned_raw, unassigned_raw, unassigned_raw)
    unassigned_view = unassigned_handle.unassignedView
    return unassigned_handle.ticketCount, unassigned_handle.platinumCount, unassigned_handle.premiumCount, unassigned_view

def teamSolved():
    solved_call = call_module.ZendeskCall()
    solved_handle = handler_module.Calculate()
    solved_raw = solved_call.teamSolved
    (solved_handle.tickets, solved_handle.ticketCount) = (solved_raw, solved_raw)
    ludzie = solved_handle.ticketsPerAgent()
    return ludzie

def teamTaken():
    taken_call = call_module.ZendeskCall()
    taken_handle = handler_module.Calculate()
    taken_raw = taken_call.teamTaken
    (taken_handle.tickets, taken_handle.ticketCount) = (taken_raw, taken_raw)
    lista = taken_handle.ticketsPerAgent()
    return lista
#==========================================================================================#
# Variables

(un_ticketCount, un_platinum, un_premium, unassigned_list) = unassigned()

# Premium and platinum together

ludzie = teamTaken()

print(ludzie)

#List of unassigned queue

#==========================================================================================#