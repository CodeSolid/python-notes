# Members are declared dynamically, even after class is "created"
def otherFunc( self ):
	print("Inside otherFunc")

class SomeClass:
	someFunc = otherFunc
			
s = SomeClass()
s.someFunc()

print (s.__class__)
