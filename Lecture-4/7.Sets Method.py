#sets -> mutable
#sets -> elements -> immutable
#unhashable sets,dict,list

"""
set.add(el)  #adds an elements
set.remove(el) #removes the elements
set.clear(el) #empties the set
set.pop(el) #pop a random value
set.union(set2) #combines both set values &returns new
set.intersection(set2) #combines common values & returns new

"""

collection = set()
collection.add(1)
collection.add(2)
collection.add(4)
collection.add("hii")
collection.add("hello")
collection.add("world")

#collection.remove(1)
#collection.clear()


print(collection.pop())
print(collection.pop())

