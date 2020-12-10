#Raymundo Sanchez
#Nov 1,2020

#this helps it connect with the main character and the followers
import mainCharacter as MC
import Followers as F

#this will start of my first section
#you have two choices to make go out at night or morning
# might die if you dont take a lantern
# after you chose the time to go out you collect the lantern 
def start(player):
    print("you just woke up late in the evening but whatever")
    input()
    print("since you need ingredients you try to chose what time to go at night or morning")
    input()
    choice = input("what time would you like to go out?\n\"A\" - go out at night\n\"B\" - wait for morning").upper()
#this just shows you what will happen if you chose A or B.
    while choice == 'A':
        print("Go out at night")
        print("you should take a lantern because you might die without it")
        input()
        print("you collected the lantern")
#this will add the lantern into you inventory
#if you go out at night without the lantern you will die.
        player.inventory.append("lantern")
        print("......")
        input()
        print("why isn't the lantern working")
        input()
        print("guess i'll get a new one")
        input()
        print("Unfortunately for you the second you turned around you slipped on a banana peel and you went dead")
        input()
        print("you dead x - x ")
        input()
        choice = input("what time would you like to go out?\n\"A\" - go out at night\n\"B\" - wait for morning").upper()
        
    if choice == 'B':
        print("go out in the morning")
        input()
        print("you feel a bit tired but decided to go out anyways")
        print("you get you backpack and go out")
        player.inventory = []
#it goes over how you are about to leave  the house
#you start to collect the last items and add them to inventory
        input()
        print("you start to look throught the room what you will need to go to the forest")
        print("you find your tool box and you realize you need tools and weapons")
        print("you decide to take four things an axe, knife, three fruits, and rope")
        player.inventory = []
        player.inventory.append("axe")
        player.inventory.append("knife")
        player.inventory.append("fuits")
        player.inventory.append("rope")
        print(player.inventory)
        input()

#this tells you that you are ready to leave.
#this should take you back to the main game but check with ronan.
        print("you are ready to go out and gather ingredients")
        input()
        #print("you start to go to the forest",player.follower[0].MC.mainCharacter+"!")
        



       

            

        
        
        
    
