#!/usr/bin/python3
from components import call_module
from components import handler_module

import eel

eel.init("web")

def unassigned():
    unassigned_call = call_module.ZendeskCall()
    unassigned_handle = handler_module.Handler()
    unassigned_raw = unassigned_call.unassigned_queue
    (unassigned_handle.tickets, unassigned_handle.view_ticket_count, \
    unassigned_handle.platinum_ticket_count, unassigned_handle.premium_ticket_count, \
    unassigned_handle.divide_ticket_count) = (unassigned_raw, unassigned_raw, \
                                         unassigned_raw, unassigned_raw, unassigned_raw)
    unassigned_tickets, transfer_tickets = unassigned_handle.divide_ticket_count
    unassigned_view = unassigned_handle.get_view('Unassigned')
    return unassigned_handle.platinum_ticket_count, unassigned_handle.premium_ticket_count, unassigned_view, unassigned_tickets, transfer_tickets

def not_answered():
    not_answered_call = call_module.ZendeskCall()
    not_answered_handle = handler_module.Handler()
    not_answered_raw = not_answered_call.not_answered
    (not_answered_handle.tickets, not_answered_handle.view_ticket_count) = (not_answered_raw, not_answered_raw)
    not_answered_view = not_answered_handle.get_view('NotAnswered')
    return not_answered_view

def team_taken():
    call = call_module.ZendeskCall()
    handle = handler_module.Handler()
    raw = call.team_taken
    (handle.tickets, handle.view_ticket_count) = (raw, raw)
    lista = handle.tickets_per_agent()
    return lista

def team_solved():
    call = call_module.ZendeskCall()
    handle = handler_module.Handler()
    raw = call.team_solved
    (handle.tickets, handle.view_ticket_count) = (raw, raw)
    ludzie = handle.tickets_per_agent()
    return ludzie

#==========================================================================================#
# Variables


@eel.expose
def test_request():
    (un_platinum, un_premium, unassigned_list, un_Tickets, trans_Tickets) = unassigned()
    taken_list = team_taken()
    solved_tickets = team_solved()
    (na_view) = not_answered()
    
    eel.pickupRate(taken_list)
    eel.unassignedCount(un_Tickets)
    eel.unassignedPlatinum(un_platinum)
    eel.unassignedPremium(un_premium)
    eel.unassignedTransfer(trans_Tickets)
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
