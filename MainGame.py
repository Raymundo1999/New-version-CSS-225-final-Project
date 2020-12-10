#Raymundo Sanchez
#Nov 1,2020


import mainCharacter as MC
import section1
import section2
import section3

#Main Character will go here
player = MC.mainCharacter()

#this will show the intro to the game
#the empty imput was included to be able to click a button to go forward
print("Hey I see your awake!")
input()
player.name = input("Name goes here: ")
print(" very unique", player.name)
print("This is your house and the country you are in is")
input()
print("actually I don't know so don't ask me")
input()
#the players name wil go here.
#MC has a name already so it will be "Mac"

#this is just the person getting introduced to the game and section1 will start.

print("you might want to know if you have died or if you were summoned to this location")
input()
print("But in truth I'm just hungry so you are going to collect ingredients")
input()
print("that way we can all come together and eat in the end of the day")
input()

print("your no hero just a person that is hungry and wants to eat")
print("Have a good day and have fun and try not to get lost I'm hungry")

print("I'm not going to go rescue you, I'll just get food and eat")
print("Anyways have fun PS: It is not my fault if you die")

#this will send you and strt you in Section1 then after it is done it will return you with a message at the end.
section1.start(player)
section2.start(player)
section3.start(player)

print ("you are back", player.name)

