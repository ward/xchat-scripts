# -*- coding: utf-8 -*-

__module_author__ = 'Ward Muylaert'
__module_name__ = 'ChanOpMsg'
__module_version__ = '0.1'
__module_description__ = 'Properly shows PRIVMSGs to [@%+]#channel'

import xchat

def chanopmsg(word, word_eol, userdata):
    if word[2][0] in ['@', '%', '+']:
        nick = word[0][1:].split('!')[0]
        # What about the same channel name on two different servers?
        channel = xchat.find_context(channel = word[2][1:])
        channel.emit_print("Channel Notice", nick, word[2], word_eol[3][1:])
        return xchat.EAT_ALL

xchat.hook_server("PRIVMSG", chanopmsg)


xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))
