#!/usr/bin/python3
from components import call_module
from components import handler_module
from components import json_module

import eel

eel.init("web")

def unassigned():
    unassigned_call = call_module.ZendeskCall()
    unassigned_handle = handler_module.Calculate()
    unassigned_raw = unassigned_call.unassignedQueue
    (unassigned_handle.tickets, unassigned_handle.ticketCount, unassigned_handle.platinumCount, unassigned_handle.premiumCount) = (unassigned_raw, unassigned_raw, unassigned_raw, unassigned_raw)
    unassigned_view = unassigned_handle.unassignedView
    return unassigned_handle.ticketCount, unassigned_handle.platinumCount, unassigned_handle.premiumCount, unassigned_view

def teamTaken():
    taken_call = call_module.ZendeskCall()
    taken_handle = handler_module.Calculate()
    taken_raw = taken_call.teamTaken
    (taken_handle.tickets, taken_handle.ticketCount) = (taken_raw, taken_raw)
    (taken_bR, taken_nM, taken_mO, taken_hW, taken_aS, taken_wN, taken_mB) = taken_handle.ticketsPerAgent()
    return taken_bR, taken_nM, taken_mO, taken_hW, taken_aS, taken_wN, taken_mB

def teamSolved():
    solved_call = call_module.ZendeskCall()
    solved_handle = handler_module.Calculate()
    solved_raw = solved_call.teamSolved
    (solved_handle.tickets, solved_handle.ticketCount) = (solved_raw, solved_raw)
    (solved_bR, solved_nM, solved_mO, solved_hW, solved_aS, solved_wN, solved_mB) = solved_handle.ticketsPerAgent()
    return solved_bR, solved_nM, solved_mO, solved_hW, solved_aS, solved_wN, solved_mB

#==========================================================================================#
# Variables

@eel.expose
def test_request():
    (un_ticketCount, un_platinum, un_premium, unassigned_list) = unassigned()
    return un_ticketCount

# Tickets taken last 12h per agent
(taken_bR, taken_nM, taken_mO, taken_hW, taken_aS, taken_wN, taken_mB) = teamTaken()

# Tickets solved last 12h per agent
(solved_bR, solved_nM, solved_mO, solved_hW, solved_aS, solved_wN, solved_mB) = teamSolved()

#List of unassigned queue

#==========================================================================================#


# @eel.expose
# def ticket_count():
#     return un_ticketCount


eel.start("index.html", size=(1280, 720))
