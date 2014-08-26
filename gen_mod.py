#!/usr/bin/python
import json

# events
from mod.event.internal import event_internal
from mod.event.object import event_object
from mod.event.remote import event_remote
# actions
from mod.action.internal import action_internal
from mod.action.object import action_object

event = {}
action = {}
for i in (event_object,
          event_remote,
          event_internal,
          action_internal,
          action_object):
	event.update(i)

for i in (action_internal,
          action_object):
	action.update(i)

with open('./event.json', 'w+') as f:
	f.write(json.dumps(event, indent=4, sort_keys=True))
with open('./action.json', 'w+') as f:
	f.write(json.dumps(action, indent=4, sort_keys=True))
