#!/usr/bin/env python
"""
recruiting.py - UDL recruiting tools
Copyright 2011, Edward D. Powell, embolalia.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import select

poll = select.poll()
channels = [('#NS-Globe', '/home/embo/Desktop/test')]
message = "this is a test"
mapping = dict()
for c in channels:
   fil = open(c[2])
   mapping.update(fil=c[1])
   poll.register(fil)
   
   
def poll(phenny, input):
   actions = poll.poll()
   for a in actions:
      channel = mapping.get(a)
      phenny.write(['MSG', channel], message)

