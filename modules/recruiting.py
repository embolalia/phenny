#!/usr/bin/env python
"""
recruiting.py - UDL recruiting tools
Copyright 2011, Edward D. Powell, embolalia.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import select, os

poll = select.poll()
channels = [('#NSGlobe', '/home/embo/Desktop/test')]
message = "this is a test"
mapping = dict()
for c in channels:
   fil = open(c[1], 'r')
   fil.seek(0, os.SEEK_END)
   mapping.update(fil=c[0])
   poll.register(fil, select.POLLIN | select.POLLPRI)
   
   
def do_poll(phenny, input):
   actions = poll.poll()
   for a in actions:
      channel = mapping.get(a)
      print "test"
      phenny.say("test")
      phenny.write(['PRIVMSG', channel], message)

def startpoll(phenny, input):
   phenny.say("Recruitment polling started.")
   do_poll(phenny, input)
startpoll.commands = ["startpoll"]
