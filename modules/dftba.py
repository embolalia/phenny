"""
dftba.py - Phenny DFT.BA Module
Author: Edward Powell, embolalia.net
About: http://inamidst.com/phenny/

This module allows for retrieving stats, shortening and lengthening dft.ba urls.
"""
import urllib
import simplejson as json

def shorten(phenny, input):
    args = input.groups()
    url = args[0]
    if len(args) == 2: code = args[1]
    if code: params = urllib.urlencode({'TARGET_URL': url, 'SOURCE_URL': code})
    else: params = urllib.urlencode({'TARGET_URL': url})
    r = urllib.urlopen('http://dft.ba/api/shorten.json', params)
    response = json.loads(r.read())['api_response']
    url = response['response']['short_url']
    if not url:
        msg = 'Uh oh. Something went wrong with your request.'
        if code: msg = msg + ' I think the code you want is already in use.'
    else:
        msg = 'http://dft.ba/' + url
    phenny.say(msg)
shorten.rule = '\.[shorten|short|shorturl|tiny|shrink] (\S+) ?(\S+)?'


def expand(phenny, input):
    url = input.group(1)
    params = urllib.urlencode({'SHORT_URL': url})
    r = urllib.urlopen('http://dft.ba/api/expand.json', params)
    longurl = json.loads(r.read())['api_response']['response']['long_url']
    phenny.say('http://dft.ba/' + url + ' redirects to ' + longurl)
expand.rule = '.*http://dft.ba/(\S+).*'
