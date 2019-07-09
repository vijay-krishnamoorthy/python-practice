print("######################### Welcome to number game #########################")
name = input("\nMay I know you name?\n")
print("Hello! ",name)
print("Before We start to play, \nknow the basics and ground rules of the game")
print("\n1. you have 6 guess\n")
print("2.The numbers will be in between 1 and 10\n")
print("3.I'll let you know if you win\n")
print("4.Each time a new number will be generated\n")
import random

for i in range(0,6):
    print(i,"guesses used")
    rand = random.randint(1,10)
    number = int(input("Take a guess!!\n"))
    if(number > rand):
        print("Your guess is too high")
    elif(number < rand):
        print("Your guess is too low")
    elif (number==rand):
        print("Your guessed it right ",name)
        print("the number I generated is ",rand)
        break
else :
    print("\nYou've LOST the game ",name)
