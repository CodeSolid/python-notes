class Employee:
	"""The Employee class holds employees 

	But not too tightly so as not to be accused of harassment"""
	empCount = 0   		# Class (static) variable

	def __init__ (self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		"""Shows the total number of employees"""
		print("Total Employees %d" % Employee.empCount)

	def displayEmployee(self):
		print("Name:  ", self.name, ", Salary: ", self.salary)
	
e = Employee("John Lockwood", 1000000)
e.displayCount()
e.displayEmployee()

print("e.__dict__ = ", str(e.__dict__))
print("e.__doc__ = ")
print(str(e.__doc__))
print("DisplayCount's doc:")
print(e.displayCount.__doc__)

print("Class ", e.__class__, " is defined in module ", e.__module__)
print("It has the following bases:", str(e.__class__.__bases__))

