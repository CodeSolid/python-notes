
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
