#myString = "This is a string."
#print(myString)
#print(type(myString))
#print(myString + " is of the data type " + str(type(myString)))
#firstString = "Rojalin"
#secondString = "Swain"
#thirdString = firstString + secondString
#print(thirdString)
#name = input("What is your name? ")
#print(name)
#color = input("What is your favorite color?  ")
#animal = input("What is your favorite animal?  ")
#print("{}, you like a {} {}!".format(name,color,animal))


userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")






















