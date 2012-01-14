# -*- coding: utf-8 -*-

__module_author__ = 'Ward Muylaert'
__module_name__ = 'GCalc'
__module_version__ = '0.2'
__module_description__ = 'Google Calculator'

import xchat
from urllib import URLopener

class MyURL(URLopener):
    version = 'Mozilla/5.0 (X11; Linux x86_64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1'

def gcalc(word, word_eol, userdata):
    baseurl = 'http://www.google.com/search?q=%s'

    # TODO: Fix freeze while loading.
    opener = MyURL()
    content = opener.open(baseurl % word_eol[1]).read()

    #xchat.prnt(content)

    lindex = content.find('<h2 class=r style="font-size:138%">')
    if lindex == -1:
        xchat.prnt('Nothing found. If this seems wrong, please debug.')
        return xchat.EAT_ALL
    lindex = lindex + len('<h2 class=r style="font-size:138%"><b>')
    rindex = content.find('</b></h2>', lindex)
    result = content[lindex:rindex]
    result = " ".join(result.split())
    result = result.replace('&nbsp;', ' ')
    result = result.replace('&#215;', '×')
    result = result.replace('<sup>', '^')
    result = result.replace('</sup>', '')
    result = result.replace('<font size=-2> </font>', ',')
    xchat.prnt("Google Calculator: %s" % result)
    return xchat.EAT_ALL

xchat.hook_command('gcalc', gcalc)

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))
