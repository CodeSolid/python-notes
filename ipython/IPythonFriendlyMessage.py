# From Python for Data Analysis, making classes IPython friendy.
class Message:
	def __init__(self, msg):
		self.msg = msg

	def __repr__(self):
		return 'Message: %s' % self.msg

# Demo
# get_ipython().magic(u'run IPythonFriendlyMessage.py')
# x = Message("Hello world")
# x
