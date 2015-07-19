# Python and IPython 

This repo is just a record of my Python and IPython notes and experiments.


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

Here's a [link](http://nbviewer.ipython.org/github/CodeSolid/python-notes/blob/master/ipython/num_py_array.ipynb) to nbviewer, displaying one of my first IPython notebooks.



## Helpful Links

[IPython Tutorial](http://ipython.org/ipython-doc/stable/interactive/tutorial.html).

[Pandas API Documentation](http://pandas.pydata.org/pandas-docs/dev/api.html).