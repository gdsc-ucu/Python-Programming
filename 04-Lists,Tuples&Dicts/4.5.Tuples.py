#immutable and mutable data types
#tuples are similar to lists except: parenthesis used() and cannot be modified
tuple=('howdy','mel','shaggy','scooby')
print(tuple[1])
print(tuple[0:2])
print(len(tuple))

#there isn;t much to talk about tuples though
#use the type function to understand difference between a tuple and a string

print(type("hello",))
print(type("hello"))
#to be revisted

#Change from list to tuple- tuple()
#change from tuple to list- list()

my_list=list((tuple))
print(my_list)
