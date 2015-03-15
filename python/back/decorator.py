class myDecorator(object):

    def __init__(self, f):
        # print ("inside myDecorator.__init__()")
        self.f = f        

    def __call__(self):
        # print ("inside myDecorator.__call__()")
        print("Entering function: " + self.f.__name__)
        self.f()
        print("Exiting function: " + self.f.__name__)

@myDecorator
def aFunction():
	print ("Inside aFunction")

aFunction()