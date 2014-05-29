__module_author__ = "Ward Muylaert"
__module_name__ = "Cycle on Empty"
__module_version__ = "0.1"
__module_description__ = "Automatically cycles when the last other person leaves a channel to attempt to get OP"

import xchat

monitoring = []

def monitorchannel(word, word_eol, userdata):
    """ No input: show all, 1 input: add/delete input depending on first
    character"""
    if len(word) == 1:
        show_channels()
    elif len(word) > 2:
        xchat.prnt("Too much input!")
    elif word[1] == "--help":
        xchat.prnt("/monitorchannel to show all currently monitored\n" +
            "/monitorchannel #channel to start monitoring the channel\n" +
            "/monitorchannel -#channel to stop monitoring the channel")
    elif word[1][0] == "-":
        remove_channel(word[1][1:])
    else:
        add_channel(word[1])
    return xchat.EAT_ALL

def add_channel(channel):
    # Todo: validate input
    monitoring.append(channel)
    xchat.prnt("Added " + channel)

def remove_channel(channel):
    try:
        monitoring.remove(channel)
        xchat.prnt("Removed " + channel)
    except ValueError:
        xchat.prnt("No such channel being monitored: " + channel)

def show_channels():
    xchat.prnt(", ".join(monitoring))

def is_monitored(channel):
    return channel in monitoring


def catch_part(word, word_eol, userdata):
    # word = [nick, host, channel, reason]
    # with reason optional
    if is_monitored(word[2]):
        channel = xchat.get_context()
        users = channel.get_list("users")
        # I believe when the last other person leaves, it will always say there
        # are two users in the channel (you + the other). Matching 1 and 2 just
        # in case though.
        if len(users) < 3:
            channel.command("cycle")
    return xchat.EAT_NONE

def catch_quit(word, word_eol, userdata):
    # word = [nick, reason, host]
    # Triggers for every channel the person was in that we are also in
    context = xchat.get_context()
    channel_string = context.get_info("channel")
    if is_monitored(channel_string):
        channel = context
        users = channel.get_list("users")
        # This one doesn't seem to trigger before the leaving takes effect
        if len(users) == 1:
            channel.command("cycle")
    return xchat.EAT_NONE


# Attach hooks
xchat.hook_print("Part", catch_part)
xchat.hook_print("Part with Reason", catch_part)
xchat.hook_print("Quit", catch_quit)

xchat.hook_command("monitorchannel", monitorchannel)

xchat.prnt("Loaded %s v%s by %s."
        % (__module_name__, __module_version__, __module_author__))