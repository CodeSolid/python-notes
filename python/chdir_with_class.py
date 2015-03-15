import os

class Chdir:         
	def __init__( self, newPath ):  
		self.savedPath = os.getcwd()		
		print ("Changing from " + self.savedPath + " to " + newPath)
		os.chdir(newPath)
		print("Path is now " + os.getcwd())

	def __del__( self ):
		print ("Changing back to " + self.savedPath)
		os.chdir( self.savedPath )

	def __exit__( self, type, value, traceback):
		print("Inside __exit__")


	def __enter__( self ):
		print("Inside __enter__")

foo = Chdir("..\\")
del foo

with  Chdir("..\\..\\") as moo:
	print("Inside with block")