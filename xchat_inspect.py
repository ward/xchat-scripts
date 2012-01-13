# -*- coding: utf-8 -*-

__module_author__ = "Ward Muylaert"
__module_name__ = "XChat Inspect"
__module_version__ = "0.1"
__module_description__ = "Print the interface of the xchat module"

import xchat

def inspect(word, word_eol, userdata):
    methods = xchat.__dict__
    for key in methods:
        print chr(2), key, chr(2), methods[key]
    return xchat.EAT_NONE

xchat.hook_command("xchatinspect", inspect)

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))
