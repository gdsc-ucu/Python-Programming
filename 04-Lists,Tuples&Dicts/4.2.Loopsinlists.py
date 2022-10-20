fruits=["oranges","mangoes","apples","pawpaws","watermelon"]
#prints all the items in the list
for i in fruits:
    print(i)
print("*****************")

#does the same thing
for i in range(len(fruits)):
    print(fruits[i])
print("#################")

#prints with the index
for i in range(len(fruits)):
    print(f"Index_{str(i)} in fruits is {fruits[i]}")

