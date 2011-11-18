#!/usr/bin/env python
"""
recruiting.py - UDL recruiting tools
Copyright 2011, Edward D. Powell, embolalia.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import select

poll = select.poll()
channels = [('#udl-dev', '/home/embo/Desktop/test')]
message = "this is a test"
mapping = dict()
for c in channels:
   fil = open(c[1])
   mapping.update(fil=c[0])
   poll.register(fil)
   
   
def do_poll(phenny, input):
   actions = poll.poll()
   for a in actions:
      channel = mapping.get(a)
      phenny.write(['PRIVMSG', channel], message)

def startpoll(phenny, input):
   do_poll(phenny, input)
   phenny.say("Recruitment polling started.")
startpoll.commands = ["startpoll"]
