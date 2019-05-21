import call_zendesk
import handler_zendesk
import json_zendesk

test_call = call_zendesk.Call().unassignedQueue()

test_response = json_zendesk.JsonOperation(test_call).load()

print(type(handler_zendesk.DataHandler(test_response).count))