#################################
####SIMPLE DUNGEON GAME v.1.2####
###########################################################################################
###########This game is a sample dungeon game, based off 'Randint/Range' functions#########
#This example is a good simple way for people to understand "For Loops" and <> within Py###
###########################################################################################

from random import randint
from random import randrange
import random
import time


#Player Set-up
print("Hello there Traveller, welcome to the 'Simple Dungeon Game'! To start, please enter your character name: ")
print("")
charname = input("What is your name? ")
print("")
print("Welcome aboard {}, now, what is your Race? ".format(charname))
print("")
charrace = input("Human/Gnome/Troll? ")
print("")
print("Ok, so you are from the {} race!".format(charrace))
print("")
time.sleep(1.5) #Set as 0 for dev purposes, change to 1.5
print("Loading Campaign...")
time.sleep(3.5) #Set as 0 for dev purposes, change to 3.5

#Plot introduction
print("You, {}, are walking through a dense forest when something grabs your foot!...".format(charname))
time.sleep(3.5) #Set as 0 for dev purposes, change to 3.5
print("OUCH!!!")
time.sleep(3.5) #Set as 0 for dev purposes, change to 3.5
print("A wild wolf bites you! You draw your sword, and attack!!!")
print("")
time.sleep(1.5) #Set as 0 for dev purposes, change to 1.5
print("**Y O U  E N T E R  T H E  B A T T L E**")

#Loop will decide player choice
swordattack = input("Do you want to attack it with your blade, {}? 'Yes' or 'No' answers.".format(charname))

for x in swordattack:
    if swordattack == "Yes":
        print("You deal some damage, {}!".format(charname))
        break

    elif swordattack == "YES":
        print("You deal some damage, {}!".format(charname))
        break
    
    elif swordattack == "yes":
        print("You deal some damage!, {}!".format(charname))
        break

    else:
        print("You try to escape, but the wolf won't let go! You swing your sword at it's body...")
        break

time.sleep(1.5) #Set as 0 for dev purposes, change to 1.5

#Decide whether player wins battle or dies
randint = random.randint(0,11)

print("")
for x in range(1):
    if randint >= 6:
        print("You roll the dice and hit %s battle points! You attack again and defeat the evil wolf!" % randint)
        break
    
    elif randint > 10:
        print("You hit a critical hit of %s points! You strike the wolf and it disolves into pieces of flesh!" % randint)
        break

    elif randint <= 6:
        print("You rolled the dice and ONLY hit %s battle points, the wolf defeats you and you die!" % randint)
        print("")
        print("G A M E  O V E R")
        quit()

#Player has to make a decision, use simple str 'For Loop'
print("")
shackwoods = input("You continue to journey through the woods and find a shack, should you investigate {}? Please write 'Yes' or 'No'".format(charname))
print("")

#Player checks shack in woods, used for simple for loop again
for x in shackwoods:
    if shackwoods == "Yes":
        print("You take a look inside the eerie and haunted shack, no one seems to live here anymore...")
        break

    else:
        print("You decide not to enter the shack, you walk around the outside of it and a trip wire goes off! Killing you in the process!")
        print("")
        print("G A M E  O V E R")
        quit()
time.sleep(2.5) #Set as 0 for dev purposes, change to 2.5

#Randint for loop to see what loot player gets
print("*{} searches the shack for loot*".format(charname))
time.sleep(5) #Set as 0 for dev purposes, change to 5
print("")
print("...")
time.sleep(2.5) #Set as 0 for dev purposes, change to 2.5
print("")

randint = random.randint(100,200)

#Finding loot in shack
for x in range(1):
    if randint >= 120:
        print("You find a standard bronze sword, {}, looks like it was used in the Great War...".format(charname))
        break
    elif randint > 190:
        print("You find a super rare dragon sword...you stare at it in pure awe...")
        break
    elif randint <= 120:
        print("You look around through sacks and old chests...you find nothing...")
        break

#Finalise Plot
time.sleep(2.5) #Set as 0 for dev purposes, change to 2.5
randint = random.randint(100,500)
print("")
print("You travel through the woods and find a town, and a sign reads 'WE WELCOME ALL {}'S!".format(charrace))
print("This looks like a cute place to settle down, you find an inn for %s gold a week...You might just get used to this..." % randint)
print("")
time.sleep(4) #Set as 0 for dev purposes, change to 4
print("T H E  E N D . . .")
quit()



