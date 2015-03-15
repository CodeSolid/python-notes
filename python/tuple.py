myTuple = (1,2,3)
# Doesn't work, tupples are immutable myTuple.append(4)
myList = list(myTuple)
myList.append(4)
print (myList)
# Doesn't work:
# myTuple2 = tupple(myList)
