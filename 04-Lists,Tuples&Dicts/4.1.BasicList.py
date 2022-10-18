#is a value that contains multiple values in an ordered sequence
list1=[1,2,3]
list2=['cat','bat','rat','elephant']
list3=[12,45,65,78,98,607,43]
print(list1)
print(list2)
print(list3)

#access elements in a list by using indexes
print(list1[0])
print(list1[-1])

#slicing
print(list2[0:3]) #prints values from the first to the third (0,1,2)-indices
#same as
print(list2[:2])
#same as
print(list2[0:-1])

#using the len() function
print(len(list1))
print(len(list2))
print(len(list3))

#changing values in lists
#using list1 as an example list1=[1,2,3]
list1[0]=4
print(list1)#replaces the value at index 0-1 to 4

#list concatenation from Automate the Boring Stuff with Python
print([1, 2, 3] + ['A', 'B', 'C'])
print(['X', 'Y', 'Z'] * 3)
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)
