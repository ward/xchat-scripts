# Name:		pmeh.py
# Version:	0.0.1
# Author:	nanotube <nanotube (at) users [dot] sourceforge [dot] net >
# Date:		2010-07-05
# Description:	Set the color of the PM tabs on message to be the same as a highlight on channel.
#
# This script sets the color of the PM windows to the 'highlight' color, on every message received therein.
# Since a message in a PM really is equivalent in "importance" to a highlight in-channel, it makes sense to make the
# PM tabs stand out with the highlight color when you receive a PM.

# SOurce: https://github.com/nanotube/xchatscripts

__module_author__ = "nanotube <nanotube (at) users [dot] sourceforge [dot] net >"
__module_name__ = "PM Equals Highlight"
__module_version__ = "0.0.1"
__module_description__ = "Set the color of the PM tabs on message to be the same as a highlight on channel."

print "\0034",__module_name__, __module_version__,"has been loaded\003"

import xchat

def on_pm(word, word_eol, userdata):
    destination = xchat.get_context()
    destination.command("gui color 3")

xchat.hook_print('Private Message to Dialog', on_pm);
xchat.hook_print('Private Action to Dialog', on_pm);

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))