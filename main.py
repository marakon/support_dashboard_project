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
    unassigned_handle.platinum_count, unassigned_handle.premium_count) = (unassigned_raw, unassigned_raw, \
                                                                        unassigned_raw, unassigned_raw)
    unassigned_view = unassigned_handle.unassigned_view()
    return unassigned_handle.ticket_count, unassigned_handle.platinum_count, unassigned_handle.premium_count, unassigned_view

def team_taken():
    call = call_module.ZendeskCall()
    handle = handler_module.Calculate()
    raw = call.team_taken
    (handle.tickets, handle.ticket_count) = (raw, raw)
    lista = handle.tickets_per_agent()
    return lista

def team_solved():
    call = call_module.ZendeskCall()
    handle = handler_module.Calculate()
    raw = call.team_solved
    (handle.tickets, handle.ticket_count) = (raw, raw)
    ludzie = handle.tickets_per_agent()
    return ludzie

#==========================================================================================#
# Variables


@eel.expose
def test_request():
    (un_ticketCount, un_platinum, un_premium, unassigned_list) = unassigned()
    eel.unassignedCount(un_ticketCount)
    eel.unassignedPlatinum(un_platinum)
    eel.unassignedPremium(un_premium)
    eel.unassignedList(unassigned_list)


# Tickets taken last 12h per agent
ludzie = team_taken()

# Tickets solved last 12h per agent
ludzie = team_solved()

#List of unassigned queue

#==========================================================================================#


# @eel.expose
# def ticket_count():
#     return un_ticketCount

eel.start("index.html", size=(1280, 720))
