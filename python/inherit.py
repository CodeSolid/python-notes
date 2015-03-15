class Animal:
	def speak(self):
		print("Generic animals don't speak")

class Dog(Animal):
	def speak(self):
		print("I am a dog, I say Woof, but...")
		Animal.speak(self)



x = Animal()
x.speak()
Dog().speak()
d = Dog()

print("isinstance(x, Animal) " + str(isinstance(x, Animal)))
print("isinstance(d, Animal) " + str(isinstance(d, Animal)))
print("isinstance(d, Dog) " + str(isinstance(d, Dog)))
print("isinstance(x, Dog) " + str(isinstance(x, Dog)))