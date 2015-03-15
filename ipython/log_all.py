
get_ipython().magic(u'ls ')
get_ipython().magic(u'cat log_all.py')
print ('session1')
quit()

print('session2')
get_ipython().magic(u'cat log_all.py')
log '--------------------------'
get_ipython().magic(u'cat log_all.py')
quit()

print('session with logstart off')
quit()

get_ipython().system(u'subl ../README.md')
get_ipython().magic(u'pwd ')
quit()

quit()

print('hi Jenniffer')
get_ipython().magic(u'cat log_all.py')
print('hi again')
get_ipython().magic(u'cat log_all.py')
quit()


get_ipython().magic(u"logstart 'delme.py'")
quit()

myfiles = get_ipython().getoutput(u'ls')
myfiles
quit()

myfiles = get_ipython().getoutput(u'ls')
myfiles.n
myfiles.p
myfiles.s
pyvar = 'hello world!'
get_ipython().system(u'echo "A python variable: {pyvar}"')
quit()

