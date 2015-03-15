# NOTE
# THIS PROGAM DOESN'T RUN.  
# I was trying to swap out a member function -- likely there's a way
# to do this but I don't understand it well enough (not that you should try in any case -- just curious)

class SomeClass:
	def someFunc(self):
		print("Inside somefunc")
	
s = SomeClass()
s.someFunc()

# Members are declared dynamically, even after class is "created"
def otherFunc( self ):
	print("Inside someotherfunc")

s.someFunc = otherFunc

s.someFunc()
