__module_author__ = 'Ward Muylaert'
__module_name__ = 'Flags'
__module_version__ = '0.1'
__module_description__ = ''

import xchat

# Country KEY is http://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
# Flag is 3 lines high, 12 '*' wide

# Colours are following mIRC's default, the list can be found at
# http://b.wardje.eu/2012/01/mirc-default-colours.html

_country_to_flag_dict = {
        'BEL': '\k01,01****\k08,08****\k04,04****\n\k01,01****\k08,08****\k04,04****\n\k01,01****\k08,08****\k04,04****'
        , 'CHN': '\k04,04**\\b\k08,04*\\b*\k04,04********\n\k04,04**\k08,04**\k04,04********\n\k04,04************'
        , 'DEU': '\k01,01************\n\k04,04************\n\k08,08************'
        , 'FRA': '\k02,02****\k00,00****\k04,04****\n\k02,02****\k00,00****\k04,04****\n\k02,02****\k00,00****\k04,04****'
        , 'GRC': '\k00,12\b+\b\k12,12***********\n\k00,00************\n\k12,12************'
        , 'ITA': '\k03,03****\k00,00****\k04,04****\n\k03,03****\k00,00****\k04,04****\n\k03,03****\k00,00****\k04,04****'
        , 'JPN': '\k00,00************\n\k00,00*****\k04,04**\k00,00*****\n\k00,00************'
        , 'LUX': '\k04,04************\n\k00,00************\n\k12,12************'
        , 'NLD': '\k05,05************\n\k00,00************\n\k02,02************'
        , 'PRT': '\k03,03****\k04,04********\n\k03,03****\k04,04********\n\k03,03****\k04,04********'
        , 'RUS': '\k00,00************\n\k02,02************\n\k04,04************'
        , 'USA': '\k00,02****\k04,04********\n\k00,02****\k00,00********\n\k04,04************'
}

def country_to_flag(countrycode):
    try:
        flag = _country_to_flag_dict[countrycode.upper()]
        flag = flag.replace('\\k', chr(3)).replace('\\b', chr(2))
        return flag
    except KeyError:
        raise LookupError

def flag(word, word_eol, userdata):
    channel = xchat.get_info('channel')
    modes = xchat.get_info('modes')
    if isinstance(modes, basestring):
        modes = modes.partition(' ')[0]
    if channel[0] == '#' and ('S' in modes or 'c' in modes):
        xchat.prnt("ERROR: Detected channel mode S or c")
        return xchat.EAT_ALL
    try:
        flag = country_to_flag(word[1]).split('\n')
        for line in flag:
            xchat.command("say " + line)
    except LookupError:
        xchat.prnt("ERROR: No such country code")
    return xchat.EAT_ALL

xchat.hook_command("flag", flag, help="/FLAG COUNTRYCODE")

xchat.prnt('Loaded %s v%s by %s.'
        % (__module_name__, __module_version__, __module_author__))

