__module_author__ = 'Ward Muylaert'
__module_name__ = 'figlet'
__module_version__ = '0.1'
__module_description__ = 'Use figlet to show letters over multiple lines'

import xchat
# For system call to figlet
from subprocess import check_output

def figlet(word, word_eol, userdata):
    try:
        # check_output raises error if non-0 returncode
        bigletters = check_output(word)
        bigletters = bigletters.split('\n')
        for line in bigletters:
            xchat.command('say ' + line)
    except:
        xchat.prnt('ERROR: Something went wrong')


xchat.hook_command('figlet', figlet)

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))

