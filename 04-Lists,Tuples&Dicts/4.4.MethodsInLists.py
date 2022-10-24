#Firstly understand Augmented Assignment Operators
#+=, -=, /=, *=

word="hello"
word+=" world"
word+=" the next is now"

print(word)

#finding a value with the index() method

list=[21,23,34,56,78,98]
print(list.index(34))

list1=['james','peter','jane']
print(list1.index("james"))

#adding values to lists is called appending or inserting
#how append works:
list2=['cats','dogs','mice']
list2.append('birds')
print(list2)
#will add birds to the list

#how insert works
list2.insert(2,'birds')
print(list2)

#removing values to lists is called remove()
list2.remove('birds')
print(list2)
#will remove the first instance of birds
list2.remove('birds')
print(list2)