# -*- coding: utf-8 -*-

__module_author__ = 'Ward Muylaert'
__module_name__ = 'Unicode'
__module_version__ = '0.3'
__module_description__ = 'Replaces random smileys with Unicode variants'

import xchat

def intercept_print(word, word_eol, userdata):
    if (word_eol[0][:3] == '###'):
        return xchat.EAT_NONE
    # surely this can be more efficient
    line = word_eol[0] \
        .replace('<3', '♥') \
        .replace('=)', 'ツ') \
        .replace('^^', '^̮^') \
        .replace('!!', '‼') \
        .replace('°C', '℃') \
        .replace('->', '→') \
        .replace('=>', '⇒') \
        .replace('(tm)', '™') \
        .replace('(r)', '®') \
        .replace('(c)', '©') \
        .replace(':dis:', 'ಠ_ಠ') \
        .replace(':cry:', 'ಥ_ಥ') \
        .replace('?!', '‽') \
        .replace(':roll:', '◔_◔') \
        .replace(':commy:', '☭') \
        .replace(':king:', '♔') \
        .replace(':zzz:', '(￣。￣)～ｚｚｚ') \
        .replace(':hugme:', '(ノ゜ω゜)ノ') \
        .replace(':fliptable:', '(╯°□°）╯︵ ┻━┻') \
        .replace('\\infty', '∞') \
        .replace('\\in', '∈') \
        .replace('\\forall', '∀') \
        .replace('\\nin', '∉') \
        .replace('\\sqrt', '√') \
        .replace('\\pm', '±') \
        .replace('\\neq', '≠')
    xchat.command(' '.join(['msg', xchat.get_info('channel'), line]))
    return xchat.EAT_ALL

# Empty command means catching normal text apparently
xchat.hook_command('', intercept_print)

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))
