#!/usr/bin/env python
"""
nfircguide.py - Reminders of command changes from Zoey to Willie
Copyright 2011, Edward Powell, embolalia.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

def unimplemented(phenny, input):
   phenny.say('Sorry, ' + input.nick + ', but I don\'t have that feature yet.')
unimplemented.rule = '(!|@)(lookup|DFTBA|newmember|active|mostonline|threads|members|gfight|tfln|slogan|lml|fml|youtube|utube|yt|urban|ud|shorturl|shorten|tiny|shrink|pul|pickup|pickupline|whois|wordmeter|convert|addword|delword)'

def twitter(phenny, input):
   phenny.say(input.nick + ', I think you meant .twit')
twitter.rule = '(!|@)twitter'

def google(phenny, input):
   phenny.say(input.nick + ', I think you meant .g')
google.rule = '(!|@)google'

def weather(phenny, input):
   phenny.say(input.nick + ', I think you meant .weather')
weather.rule = '(!|@)weather'

def help(phenny, input):
   phenny.say(input.nick + ', try /msg Willie .commands')
help.rule = '(!|@)(help|cmds|cmd|commands|command)'

def calc(phenny, input):
   phenny.say(input.nick + ', I think you meant .c')
calc.rule = '(!|@)calc'

def time(phenny, input):
   phenny.say(input.nick + ', I think you meant .t')
time.rule = '(!|@)time'

def tweetwatch(phenny, input):
   phenny.say(input.nick + ', I think you meant .tweetwatcher')
tweetwatch.rule = '(!|@)tweetwatcher'

def on(phenny, input):
   phenny.say(input.nick + ', I don\'t really work that way. Sorry.')
on.rule = '(!|@)(on|off)'
