#!/usr/bin/env python
"""
wa.py - NationStates WA tools for Phenny
Copyright 2011, Edward D. Powell, embolalia.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import MySQLdb

db = MySQLdb.connect(host="embolalia.net", user="bot", passwd="abotabot", db="WA")
cur = db.cursor()

def whats(phenny, input):
   #Retrieve resolution number and council
   w, abbr = input.groups()
   cur.execute("SELECT * FROM ABBRS WHERE Abbr = \"" + abbr + "\"")
   result = cur.fetchone()
   
   if result is None:
      phenny.say("Your guess is as good as mine, mate.")
   else:
      council, number = result[0], result[1]
      num = str(number)
   
      #Look up full resolution name
      select = "SELECT Name FROM RESOLUTIONS WHERE Council = \'"
      cur.execute(select + council + "\' AND Number = " +  num)
      result = cur.fetchone()
      name = result[0]
    
      if council == 'G': council = 'GA'
      else: council == 'SC'
      phenny.say(abbr + " is " + council + '#' + num + ", " + name)
      
whats.rule = ('$nick', ['whats', 'what\'s'], r'(.*)')

def sc(phenny, input):
   res = match.group(2)
   num = int(res) - 1
   link = "http://www.nationstates.net/page=WA_past_resolutions/council=2/start="
   link = link + str(res)
   phenny.say(link)

link.commands = ["sc"]
