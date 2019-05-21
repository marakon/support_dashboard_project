import call_zendesk
import handler_zendesk
import json_zendesk

test_call = call_zendesk.Call().myOpenTickets()

test_response = json_zendesk.JsonOperation(test_call).load()

file_ready = handler_zendesk.DataHandler(test_response).ticketsDict()

print(file_ready)