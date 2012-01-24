# -*- coding: utf-8 -*-

__module_author__ = 'Ward Muylaert'
__module_name__ = 'XChatInspect'
__module_version__ = '0.1'
__module_description__ = 'Print the interface of the xchat module'

import xchat

def inspect(word, word_eol, userdata):
    methods = xchat.__dict__
    xchat.prnt('xchat module:')
    for key in sorted(methods.iterkeys()):
        xchat.prnt('%s%s%s: %s' % (chr(2), key, chr(2), methods[key]))
    context = xchat.get_context()
    methods = dir(context)
    xchat.prnt('context:')
    for key in sorted(methods):
        xchat.prnt('%s%s%s' % (chr(2), key, chr(2)))
    return xchat.EAT_NONE

xchat.hook_command('xchatinspect', inspect)

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))
