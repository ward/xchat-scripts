__module_author__ = 'Ward Muylaert'
__module_name__ = 'AllAway'
__module_version__ = '0.1'
__module_description__ = 'Sets you away on all the servers you are connected to.'

import xchat

def allaway(word, word_eol, userdata):
    channels = xchat.get_list('channels')
    for channel in channels:
        # Channel type 1 is a server, meaning we'll do it in every status tab
        # Second check is to make sure we are connected
        if channel.type == 1 and channel.context.get_info('server') != None:
            channel.context.command(word_eol[0][3:]) 
    return xchat.EAT_ALL


xchat.hook_command('allaway', allaway)
xchat.hook_command('allback', allaway)

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))
