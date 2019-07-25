#!/usr/bin/python3
from components import call_module
from components import handler_module

import eel

eel.init("web")

def unassigned():
    unassigned_call = call_module.ZendeskCall()
    unassigned_handle = handler_module.Calculate()
    unassigned_raw = unassigned_call.unassigned_queue
    (unassigned_handle.tickets, unassigned_handle.ticket_count, \
    unassigned_handle.platinum_count, unassigned_handle.premium_count, \
    unassigned_handle.transfer_count) = (unassigned_raw, unassigned_raw, \
                                         unassigned_raw, unassigned_raw, unassigned_raw)
    unassigned_view = unassigned_handle.unassigned_view()
    return unassigned_handle.ticket_count, unassigned_handle.platinum_count, unassigned_handle.premium_count, unassigned_handle.transfer_count, unassigned_view

def not_answered():
    not_answered_call = call_module.ZendeskCall()
    not_answered_handle = handler_module.Calculate()
    not_answered_raw = not_answered_call.not_answered
    (not_answered_handle.tickets, not_answered_handle.ticket_count) = (not_answered_raw, not_answered_raw)
    not_answered_view = not_answered_handle.not_answered_view()
    return not_answered_view, not_answered_handle.ticket_count

def team_taken():
    call = call_module.ZendeskCall()
    handle = handler_module.Calculate()
    raw = call.team_taken
    (handle.tickets, handle.ticket_count) = (raw, raw)
    lista = handle.tickets_per_agent()
    print(lista)
    return lista

def team_solved():
    call = call_module.ZendeskCall()
    handle = handler_module.Calculate()
    raw = call.team_solved
    (handle.tickets, handle.ticket_count) = (raw, raw)
    ludzie = handle.tickets_per_agent()
    print(ludzie)
    return ludzie

#==========================================================================================#
# Variables


@eel.expose
def test_request():
    (un_ticketCount, un_platinum, un_premium, un_transfer, unassigned_list) = unassigned()
    taken_list = team_taken()
    solved_tickets = team_solved()
    (na_view, na_count) = not_answered()
    
    print(solved_tickets)
    eel.pickupRate(taken_list)
    eel.unassignedCount(un_ticketCount)
    eel.unassignedPlatinum(un_platinum)
    eel.unassignedPremium(un_premium)
    eel.unassignedTransfer(un_transfer)
    eel.unassignedList(unassigned_list)
    eel.notAnsweredList(na_view)

# Tickets taken last 12h per agent
ludzie = team_taken()

# Tickets solved last 12h per agent
ludzie = team_solved()

#List of unassigned queue

#==========================================================================================#


# @eel.expose
# def ticket_count():
#     return un_ticketCount

eel.start("index.html", size=(1920, 1080))
