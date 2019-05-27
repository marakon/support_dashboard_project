#!/usr/bin/python3
from components import call_module
from components import handler_module

def unassigned():
    unassigned_call = call_module.ZendeskCall()
    unassigned_handle = handler_module.Calculate()
    unassigned_raw = unassigned_call.unassigned_queue
    (unassigned_handle.tickets, unassigned_handle.ticketCount,
    unassigned_handle.platinumCount, unassigned_handle.premiumCount) = (unassigned_raw, unassigned_raw,
                                                                        unassigned_raw, unassigned_raw)
    unassigned_view = unassigned_handle.unassigned_view
    return unassigned_handle.ticketCount, unassigned_handle.platinumCount, unassigned_handle.premiumCount, unassigned_view

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

def jira():
    call = call_module.JiraCall()
    return call.view_jira_details
#==========================================================================================#
# Variables

(un_ticketCount, un_platinum, un_premium, unassigned_list) = unassigned()

# Premium and platinum together

ludzie_taken = team_taken()
ludzie_solved = team_solved()
print(ludzie_taken)
print(ludzie_solved)

case = jira()
print(case)


#List of unassigned queue

#==========================================================================================#