#Raymundo Sanchez
#Nov 29,2020
#this will connect with the other idles
import mainCharacter as MC
import Followers as F
#this will help the game start for this section
def start(player):

    print("you arrive to the forest")
    input()
    print("the second you enter the forest you tripped on a rock")
    input()
    print(" you kick it but after you turn to leave it changes form and decided to kick you back")
    input()
    print("you realize it's a mimic it gets mad at you for kicking him so he kicked you back")
    print("you apologize to him but then he asks if he can go with you")
    print("He says because he is board and doesn't have anything to do")
    choice = input("Do you let the mimic follow you?\n\"A\" - Yes follow me\n\"B\" - No don't follow me")
#this just shows you what will happen if you chose A or B.
    if choice == 'A':
        print("OK you can follow me")
        print("Just don't eat the stuff we will collect until later")
        input()
        print("Ok lets go")
        player.team.append(F.Followers("mimic"))
        #player.player.append(F.player("Mimic") )
#if you choose "B" you will end the game aince you need the follower

    while choice == 'B':
        print("No don't come with me")
        input()
        print("leave")
        print("I said good day sir!")
        print("you got stabbed to death by mimic")
        input()
        print("try again")
        input()
        choice = input("Do you let the mimic follow you?\n\"A\" - Yes follow me\n\"B\" - No don't follow me")
        
#this will collect three mushrooms and add it to the player storage or inventory
        print("we need to collect three mushroooms")
        input()
        print("you will be collecting the food items since I already have the tools")
        input()
        print("Here are the mushrooms get them")
        player.inventory = []
        player.inventory.append("mushroom")
        player.inventory.append("mushroom")
        player.inventory.append("mushroom")
        print(player.inventory)
#this will get you ready to go home but before getting home we need honey that is out side the house.
        print("we should get ready to go home but on the way we need to collect honey")
        input()
        #print("Let's go towards my house", player.team[0].name+"!")
