__module_author__ = 'Ward Muylaert'
__module_name__ = 'Colourwheel'
__module_version__ = '0.1'
__module_description__ = 'Give an overview of the colours available'

import xchat

def colourwheel(word, word_eol, userdata):
    colours = '\k01,0000\k00,0101\k00,0202\k01,0303\k01,0404' \
            '\k01,0505\k01,0606\k01,0707\k01,0808\k01,0909\k01,1010' \
            '\k01,1111\k01,1212\k01,1313\k01,1414\k01,1515'
    colours = colours.replace('\\k', chr(3))
    xchat.prnt(colours)
    return xchat.EAT_ALL

xchat.hook_command('colourwheel', colourwheel)

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))
