# Python and IPython 
## Notes and Experiments

[IPython Tutorial](http://ipython.org/ipython-doc/stable/interactive/tutorial.html).

# Configuration:

Note that ipy_user_conf.py is deprecated now -- so you should ignore documentation that references it.

On a new machine:

ipython profile create # creates default profile

Some lines from my ipython_config:

<pre>
# Start logging to the given file in append mode.
c.TerminalInteractiveShell.logappend = '/Users/johnlo/Dropbox/science/python/ipython/log_all.py'

# Set the editor used by IPython (default to $EDITOR/vi/notepad).
c.TerminalInteractiveShell.editor = '/usr/bin/subl'
</pre>

Note:  For the editor, I could not get this to work in qtconsole, so there I use !subl --> works fine!


