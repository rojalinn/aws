#myFruitList = ["apple", "banana", "cherry"]
#print(myFruitList)
#print(type(myFruitList))
#print(myFruitList[0])
#print(myFruitList[1])
#print(myFruitList[2])
#myFruitList[2] = "orange"
#print(myFruitList)
#myFinalAnswerTuple = ("apple", "banana", "pineapple")
#print(myFinalAnswerTuple)
#print(type(myFinalAnswerTuple))
#print(myFinalAnswerTuple[0])
#print(myFinalAnswerTuple[1])
#print(myFinalAnswerTuple[2])
#myFavoriteFruitDictionary = {
 # "Akua" : "apple",
 # "Saanvi" : "banana",
 # "Paulo" : "pineapple"
#}
#print(myFavoriteFruitDictionary)
#print(type(myFavoriteFruitDictionary))
#print(myFavoriteFruitDictionary["Akua"])
#print(myFavoriteFruitDictionary["Saanvi"])
#print(myFavoriteFruitDictionary["Paulo"])


#myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
#for item in myMixedTypeList:
   # print("{} is of the data type {}".format(item,type(item)))
    
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
print("Count to 10!")
for x in range (0, 11):
    print(x)






















