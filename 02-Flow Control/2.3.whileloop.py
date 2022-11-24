#Want a block to execute over and over, a while statement can do that for you
#the code will execute as long as the condition is True eg
count=0
#condition
while count<5: #don't forget the :
    print("Hey my people")
    count+=1 #increment statement
             #BE CAREFUL: # +=1 is different from =+
    #alternatively
    #count=count+1

#an annoying loop that asks you to enter "your name"
name=""
while name!="your name":
    print("Please enter 'your name'")
    name=input()
    #alternatively name=str(input("Please enter 'your name'":)
print("Thank you so much")

#using break and or an if statement
while True:
    name=str(input("Please enter 'your name':"))
    if name=="your name":
        break
print("Thank you so much")

#using continue
while True:
    name=str(input("Please enter your name:"))
    if name!="Jasper":
        continue
    password=str(input("Please enter your password:"))
    if password=="ashaba":
        break
print("Access Granted to user")

#Remember Truthy and Falsey values
#all empty and 0 values are false

#visit the while statement while variable:
name=''
while not name:
    name=str(input("Please enter your name:"))
    if name:
        guestsnumber=int(input("Please enter number of guests:"))
        if guests:
            print(f"Please plan for {guestsnumber} geusts")
print("Done with the project")

#extra while loops
#inintialize the beginning with one
i = 1
#end is 6
while i < 6:
  print(i)
  #when it reaches 3 it will stop
  if i == 3:
    break
  i += 1

#end of while loop class
