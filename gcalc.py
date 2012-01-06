# -*- coding: utf-8 -*-

__module_author__ = 'Ward Muylaert'
__module_name__ = 'GCalc'
__module_version__ = '0.1'
__module_description__ = 'Google Calculator'

import xchat
from urllib import URLopener

class MyURL(URLopener):
    version = 'GCalc'

def gcalc(word, word_eol, userdata):
    baseurl = 'http://www.google.com/search?q=%s'

    # TODO: Fix freeze while loading.
    opener = MyURL()
    content = opener.open(baseurl % word_eol[1]).read()

    lindex = content.find('<h2 class="r" dir="ltr" style="font-size:138%">')
    if lindex == -1:
        xchat.prnt('Nothing found. If this seems wrong, please debug.')
        return xchat.EAT_ALL
    lindex = lindex + len('<h2 class="r" dir="ltr" style="font-size:138%">')
    rindex = content.find('</h2>', lindex)
    result = content[lindex:rindex]
    result = " ".join(result.split())
    result = result.replace('&nbsp;', ' ')
    result = result.replace('&#215;', '×')
    result = result.replace('<sup>', '^')
    result = result.replace('</sup>', '')
    xchat.prnt("Google Calculator: %s" % result)
    return xchat.EAT_ALL

xchat.hook_command('gcalc', gcalc)

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))
