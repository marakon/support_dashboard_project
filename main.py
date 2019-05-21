import call_zendesk
import handler_zendesk
import json_zendesk
import eel

eel.init("web")

test_call = call_zendesk.Call().unassignedQueue()

test_response = json_zendesk.JsonOperation(test_call).load()

<<<<<<< HEAD:test.py
print(type(handler_zendesk.DataHandler(test_response).count))
=======
@eel.expose
def ticket_count():
    return handler_zendesk.DataHandler(test_response).count

eel.start("index.html", size=(600, 600))
>>>>>>> f76443a4de22eaef3a0c254bb526afa2676c31ff:main.py
