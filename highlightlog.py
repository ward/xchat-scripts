__module_author__ = 'Ward Muylaert'
__module_name__ = 'Highlightlog'
__module_version__ = '0.1'
__module_description__ = 'Logs highlights to a window, per-server basis.'

import xchat

def catch_highlight(word, word_eol, userdata):
    # Input string ends up being
    # NICK line of text USERMODE
    nick = word[0]
    text = word[1]
    channel = xchat.get_info('channel')
    server = xchat.get_info('server')
    highlighttab = xchat.find_context(channel='@highlights')
    if not highlighttab:
        xchat.command('NEWSERVER -noconnect @highlights')
        highlighttab = xchat.find_context(channel='@highlights')
    highlighttab.prnt('%s/%s <%s> %s' % (server, channel, nick, text))
    return xchat.EAT_NONE


xchat.hook_print('Channel Msg Hilight', catch_highlight)
xchat.hook_print('Channel Action Hilight', catch_highlight)

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))

