#!/usr/bin/env python
# coding=utf-8
"""
calc.py - Phenny Calculator Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import re, string, web

r_result = re.compile(r'(?i)<A NAME=results>(.*?)</A>')
r_tag = re.compile(r'<\S+.*?>')

subs = [
	(' in ', ' -> '),
	(' over ', ' / '),
	(u'£', 'GBP '),
	(u'€', 'EUR '),
	('\$', 'USD '),
	(r'\bKB\b', 'kilobytes'),
	(r'\bMB\b', 'megabytes'),
	(r'\bGB\b', 'kilobytes'),
	('kbps', '(kilobits / second)'),
	('mbps', '(megabits / second)')
]

def calc(phenny, input):
	"""Use the Frink online calculator."""
	q = input.group(2)
	if not q:
		return phenny.say('0?')

	query = q[:]
	for a, b in subs:
		query = re.sub(a, b, query)
	query = query.rstrip(' \t')

	precision = 5
	if query[-3:] in ('GBP', 'USD', 'EUR', 'NOK'):
		precision = 2
	query = web.urllib.quote(query.encode('utf-8'))

	uri = 'http://futureboy.us/fsp/frink.fsp?fromVal='
	bytes = web.get(uri + query)
	m = r_result.search(bytes)
	if m:
		result = m.group(1)
		result = r_tag.sub('', result) # strip span.warning tags
		result = result.replace('&gt;', '>')
		result = result.replace('(undefined symbol)', '(?) ')

		if '.' in result:
			try: result = str(round(float(result), precision))
			except ValueError: pass

		if not result.strip():
			result = '?'
		elif ' in ' in q:
			result += ' ' + q.split(' in ', 1)[1]

		phenny.say(q + ' = ' + result[:350])
	else: phenny.reply("Sorry, can't calculate that.")
	phenny.say('Note that .calc is deprecated, consider using .c')
calc.commands = ['calc']
calc.example = '.calc 5 + 3'

def c(phenny, input):
	"""Google calculator."""
	if not input.group(2):
		return phenny.reply("Nothing to calculate.")
	q = input.group(2).encode('utf-8')
	q = q.replace('\xcf\x95', 'phi') # utf-8 U+03D5
	q = q.replace('\xcf\x80', 'pi') # utf-8 U+03C0
	uri = 'http://www.google.com/ig/calculator?q='
	bytes = web.get(uri + web.urllib.quote(q))
	parts = bytes.split('",')
	answer = [p for p in parts if p.startswith('rhs: "')][0][6:]
	if answer:
		answer = answer.decode('unicode-escape')
		answer = ''.join(chr(ord(c)) for c in answer)
		answer = answer.decode('utf-8')
		answer = answer.replace(u'\xc2\xa0', ',')
		answer = answer.replace('<sup>', '^(')
		answer = answer.replace('</sup>', ')')
		answer = web.decode(answer)
		phenny.say(answer)
	else: phenny.say('Sorry, no result.')
c.commands = ['c']
c.example = '.c 5 + 3'

def py(phenny, input):
	query = input.group(2).encode('utf-8')
	uri = 'http://tumbolia.appspot.com/py/'
	answer = web.get(uri + web.urllib.quote(query))
	if answer:
		phenny.say(answer)
	else: phenny.reply('Sorry, no result.')
py.commands = ['py']

def wa(phenny, input):
    """Wolfram Alpha calculator"""
	if not input.group(2):
		return phenny.reply("No search term.")
	query = input.group(2).encode('utf-8')
	uri = 'http://tumbolia.appspot.com/wa/'
	answer = web.get(uri + web.urllib.quote(query.replace('+', '%2B')))
	if answer:
		# test case 1:
		# 	input: .wa today+1 week
		#	output: today+1 week;Tuesday, December 27, 2011;12\/27\/2011  (month\/day\/year);7 days from now;1 week from now;5 weekdays from now;361st day;52nd week;start of Soviet War in Afghanistan (1979): 32nd anniversary;Radio City Music Hall opens (1932): 79th anniversary;Spanish Constitution of 1978 is ratified (1978): 33rd anniversary;Rome and Vienna airport attacks (1985): 26th anniversary;1939 Erzincan earthquake (1939): 72nd anniversary;sunrise->7:50 am CST, sunset->5

		# test case 2:
		#	input: .wa circumference of the sun * pi
		#	output: Sun->equatorial circumference pi;8.531 million miles;1.373&times;10^7 km  (kilometers);1.373&times;10^10 meters;45.79 light seconds;Light travel time t in vacuum from t = x\/c:, ->46 seconds;Light travel time t in an optical fiber t = 1.48x\/c:, ->1.1 minutes

		# output seems to be "interpreted input;output;different way of writing;additional information;..;..;..;..;..;more additional information"
		waOutputArray = string.split(answer, ";")

		phenny.say("[DEVMSG]raw answer: "+answer)
		phenny.say(waOutputArray[0]+" = "+waOutputArray[1])
		waOutputArray = []


	else: phenny.reply('Sorry, no result.')
wa.commands = ['wa']
wa.example = '.wa circumference of the sun * pi'

if __name__ == '__main__':
	print __doc__.strip()
