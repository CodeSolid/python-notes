class SomeClass:
	def someFunc(self):
		print("Inside somefunc")
		print(str(self))

s = SomeClass()
s.someFunc()

# Members are declared dynamically, even after class is "created"
s.x = 10
print(s.x * 2)
del s.x

