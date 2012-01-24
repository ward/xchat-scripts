__module_author__ = 'Ward Muylaert'
__module_name__ = 'Flags'
__module_version__ = '0.1'
__module_description__ = ''

import xchat

_country_to_flag_dict = {
        'BEL': '\k01,01****\k08,08****\k04,04****\n\k01,01****\k08,08****\k04,04****\n\k01,01****\k08,08****\k04,04****'
        , 'FRA': '\k02,02****\k00,00****\k04,04****\n\k02,02****\k00,00****\k04,04****\n\k02,02****\k00,00****\k04,04****'
        , 'JPN': '\k00,00************\n\k00,00*****\k04,04**\k00,00*****\n\k00,00************'
        , 'LUX': '\k04,04************\n\k00,00************\n\k12,12************'
        , 'NLD': '\k05,05************\n\k00,00************\n\k02,02************'
        , 'USA': '\k00,02****\k04,04********\n\k00,02****\k00,00********\n\k04,04************'
}

def country_to_flag(countrycode):
    try:
        flag = _country_to_flag_dict[countrycode]
        flag = flag.replace('\\k', chr(3))
        return flag
    except KeyError:
        raise LookupError

def flag(word, word_eol, userdata):
    try:
        flag = country_to_flag(word[1]).split('\n')
        for line in flag:
            xchat.prnt(line)
    except LookupError:
        xchat.prnt("ERROR: No such country code")
    return xchat.EAT_ALL

xchat.hook_command("flag", flag)

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))

