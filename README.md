# About

These are some scripts for [XChat](http://xchat.org/), an IRC client.
It really is just whatever
comes in my mind and seems useful at the time, made to quickly work.
Testing is minimal, but what ends up in it, should work.

# Usage

XChat only autoloads scripts that it finds in its directory (on Linux
this is `~/.xchat2/`). So you can either copy a script you want into the
directory yourself or you can opt to clone the entire repository (eg into
`~/.xchat2/scripts/`) and then symlinking the ones you want. The upside of
the latter approach is that you can update the scripts by issuing
`git pull`.

# Add Your Own

I'd like to keep this repo Python only, so if you want something added here,
please try to use Python. The XChat plugin uses Python 2 still, so keep
that in mind as well. For the XChat documentation, I refer you to

* [XChat Python](http://xchat.org/docs/xchatpython.html)
* [XChat C++](http://xchat.org/docs/plugin20.html) (handy for some
  things that are undocumented in the Python docs)
