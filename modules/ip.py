#!/usr/bin/env python
# coding=utf-8
"""
ip.py - Phenny IP Lookup Module
Copyright 2011, Dimitri Molenaars, TyRope.nl
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import re, string, web

def ip(phenny, input):
    """IP Lookup tool"""
	if not input.group(2):
		return phenny.reply("No search term.")
	query = input.group(2).encode('utf-8')
	uri = 'http://www.rscript.org/lookup.php?type=ipdns&ip='
	answer = web.get(uri + web.urllib.quote(query.replace('+', '%2B')))
	if answer:
		invalid = re.search("(?:INVALID: )([\S ]*)", answer)
		if invalid:
			response = "[IP/Host Lookup] "+invalid
		else:
			#parse stuffs.
			host = re.search("(?:Hostname:[ ]?)([\S ]*)(?:\r)", answer)
			isp = re.search("(?:ISP:[ ]?)([\S ]*)(?:\r)", answer)
			org = re.search("(?:Organization:[ ]?)([\S ]*)(?:Services:)", answer)
			typ = re.search("(?:Type:[ ]?)([\S ]*)(?:\r)", answer)
			assign = re.search("(?:Assignment:[ ]?)([\S ]*)(?:\r)", answer)
			city = re.search("(?:City:[ ]?)([\S ]*)(?:\r)", answer)
			state = re.search("(?:State/Region:[ ]?)([\S ]*)(?:\r)", answer)
			country = re.search("(?:Country:[ ]?)([\S ]*)(?:  \r)", answer)

			response = "[IP/Host Lookup] Hostname: "+host+" | ISP: "+isp+" | Organization: "+org+" | Type: "+typ+" | Assignment: "+assign+" | Location: "+city+", "+state+", "+country+"."
		phenny.say(response)
	else:
		phenny.reply('Sorry, no result.')
wa.commands = ['iplookup']
wa.example = '.iplookup 8.8.8.8'

if __name__ == '__main__':
	print __doc__.strip()