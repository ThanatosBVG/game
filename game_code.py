from typing import List, Literal, Union
import random
import time
import sys
import pydash
from termcolor import cprint
from termcolor import colored

# List of Items found throughout the crawler
# mystery vial
# Sword
# regular clothes

def delay_print(words):
    for l in words:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.005)


def inputFromList(question, allowed_responses):
    
    delay_print(question)
    ans = input().lower()
    
    # Special case: `None` means allow anything
    if allowed_responses == None:
        return ans

    while ans not in allowed_responses:
        delay_print(f"You must say one of these: {allowed_responses}\n")
        ans = input().lower()
    
    return ans

def startoverAction(answer):
            delay_print("You awake in a dark room, You vaguely remember this place.\n")
            delay_print("You look around and see a pile of clothes, a chest, and a window.\n")
            p.health = 30
            p.armor = 10
            p.inventory = []
            p.location = "darkroom"
            p.prompt = "Do you check the pile of clothes, the chest, or the window "
            p.allowed_resps = ["pile of clothes", "chest", "window"]

def darkroomAction(answer):
    if answer == "pile of clothes":
        delay_print("You realise you are naked and don the clothes.\n")
        if "regular clothes" not in p.inventory:
            p.inventory.append("regular clothes")
            cprint(f"Inventory:{p.inventory}", "green")
            p.armor = p.armor + 1
            cprint(f"Armor:{p.armor}", "cyan")
        p.prompt = "Now do you go to the window or check the chest? "
        p.allowed_resps = ["window","chest"]
    if answer == "window":
        delay_print("As you walk to the window, you see designs in the window, you also see a door that you didn't see before \n")
        p.location = "walkingroom"
        p.prompt = "Do you attempt to open the door or go to the window?\n"
        p.allowed_resps = ["go to the window","open the door"]
    if answer == "chest":
        delay_print("You find a mysterious vial with a red liquid in it.\n")
        p.location = "roomwithvial"
        p.prompt = "Do you drink the vial?"
        p.allowed_resps = ["yes","no"]

def darkroom2Action(answer):
    if answer == "explore":
        delay_print("You notice a second chest has appeared in the room, but everything else looks the same\n")
        p.location = "darkroom2"
        p.prompt = "What would you like to do?"
        p.allowed_resps = ["second chest", "chest", "pile of clothes", "window", "door"]
    if answer == "chest":
        delay_print("You walk over to the chest you find the vial in and find another vial\n")
        p.location = "roomwithvial"
        p.prompt = "Do you drink the vial?"
        p.allowed_resps = ["yes","no"]
    if answer == "second chest":
        delay_print("You are curious about this new chest and go over to it cautiously\n")
        delay_print("You open the chest and find a set of half chain armor\n")
        p.location = "darkroom2"
        p.prompt = "Do you don the armor?\n"
        p.allowed_resps = ["put it on", "put it back"]
    if answer == "window":
        delay_print("You walk over to the window, noticing the designs have changed but still looks breakable\n")
        delay_print("You also see the door you found last time\n")
        dieroll = random.randint(1,20)
        cprint(dieroll, "magenta")
        if dieroll >= 18:
            delay_print("The window breaks and you fall out into an empty courtyard\n")
            delay_print("You look around and see a wagon, a gate, and a door back into the building you just fell out of \n")
            p.health = p.health - 10
            cprint(f"HP:{p.health}", "red")
            p.location = "courtyard"
            p.prompt = "Do you check the wagon, go to the gate, or check the door "
            p.allowed_resps = ["wagon","gate","door"]
        else:
            p.location = "atwindow"
            p.prompt = "Do you try to break it or open the door?"
            p.allowed_resps = ["break it", "open door"]
    if answer == "put it on":
        if "Half Chain" not in p.inventory:
            p.inventory.append("Half Chain")
            cprint(f"Inventory:{p.inventory}", "green")
            p.armor = 16
            cprint(f"Armor:{p.armor}", "cyan")
            delay_print("You put the armor on and feel a wierd sensation, almost as if the armor doesn't have a weight")
            p.location = "darkroom2"
            p.prompt = "What would you like to do now?\n"
            p.allowed_resps = ["chest", "pile of clothes", "window", "door"]
    if answer == "put it back":
        delay_print("You set the armor down and suddenly the chest disappears")
        p.location = "darkroom2"
        p.prompt = "What would you like to do now?\n"
        p.allowed_resps = ["chest", "pile of clothes", "window", "door"]

        

def opendoorAction(answer):
    if answer == "go to the window":
        dieroll = random.randint(1,20)
        cprint(dieroll, "magenta")
        if dieroll >= 18:
            delay_print("The window breaks and you fall out into an empty courtyard\n")
            delay_print("You look around and see a wagon, a gate, and a door back into the building you just fell out of \n")
            p.health = p.health - 10
            cprint(f"HP:{p.health}", "red")
            p.location = "courtyard"
            p.prompt = "Do you check the wagon, go to the gate, or check the door "
            p.allowed_resps = ["wagon","gate","door"]
        else:
            delay_print("The window is cracked and looks like you can break it, but you don't see anything outside\n")
            p.location = "atwindow"
            p.prompt = "Do you try to break it or open the door?"
            p.allowed_resps = ["break it", "open door"]
    elif answer == "open the door":
        dieroll = random.randint(1,20)
        cprint(dieroll, "magenta")
        if dieroll >= 14:
            delay_print("You have sucessfully opened the door!\n")
            delay_print("You step out of the room onto a landing with a staircase going up, and one going down \n")
            p.location = "landing"
            p.prompt = "Do you go up or down the stairs? "
            p.allowed_resps = ["up","down"]
        else:
            delay_print("The door is wedged but you feel it give a bit\n")

def landingAction(answer):
    if answer == "up":
        delay_print("you walk up the staircase to find a hallway that splits three ways\n")
        p.location = "triplehall"
        p.prompt = "Which way do you choose to go? "
        p.allowed_resps = ["left", "right", "forward","back"]
    elif answer == "down":
        delay_print("You descend the staircase to find a room with three doors in it\n")
        p.location = "threedoor"
        p.prompt = "Which door do you choose to go into?\n"
        p.allowed_resps = ["first", "second", "third","back"]

def triplehallAction(answer):
    if answer == "left":
        delay_print("You turn left and start walking down the left hallway until you come up to another intersection\n")
        p.location = "losthall"
        p.prompt = "Which way do you choose to go? "
        p.allowed_resps = ["left", "right", "forward","back"]
    elif answer == "forward":
        delay_print("You go forward for a ways until you see another intersection\n")
        p.location = "losthall"
        p.prompt = "Which way do you choose to go? "
        p.allowed_resps = ["left", "right", "forward","back"]
    elif answer == "right":
        delay_print("You turn right and start walking down the right hallway until you come up to another intersection\n")
        p.location = "losthall"
        p.prompt = "Which way do you choose to go? "
        p.allowed_resps = ["left", "right", "forward","back"]
    elif answer == "back":
        delay_print("You get an ominous feeling about this section of the building and turn back around and go back down the stairs to the landing\n")
        p.location = "landing"
        p.prompt = "Which way do you choose to go? "
        p.allowed_resps = ["up","down"]

def losthallAction(answer):
    if answer == "left":
        delay_print("You turn left and start walking down the left hallway until you come up to another intersection\n")
        p.location = "losthall"
        p.prompt = "Which way do you choose to go? "
        p.allowed_resps = ["left", "right", "forward","back"]
    elif answer == "forward":
        delay_print("You go forward for a ways until you see another intersection\n")
        p.location = "losthall"
        p.prompt = "Which way do you choose to go? "
        p.allowed_resps = ["left", "right", "forward","back"]
    elif answer == "right":
        delay_print("You turn right and start walking down the right hallway until you come up to another intersection\n")
        p.location = "losthall"
        p.prompt = "Which way do you choose to go? "
        p.allowed_resps = ["left", "right", "forward","back"]
    elif answer == "back":
        delay_print("You get an ominous feeling about this section of the building and turn back around\n")
        p.location = "triplehall"
        p.prompt = "Which way do you choose to go? "
        p.allowed_resps = ["left","right", "forward", "back"]

def threedoorAction(answer):
    if answer == "first":
        if "mystery vial" not in p.inventory:
            delay_print("You open the door and find an armored cultist that turns upon hearing the door open\n")
            delay_print("he shouts, 'Hey, How did you get out!' he draws his club and hits you over the head\n")
            delay_print("You see stars and your vision dims as you fall over from the blow\n")
            startoverAction(answer)
        else: 
            "mystery vial" in p.inventory
            delay_print("You open the door and find an armored cultist that turns upon hearing the door open\n")
            delay_print("You only have a vial in your pocket to defend yourself\n")
            p.location = "firstroom"
            p.prompt = "Do you throw the vial or attempt to grapple the cultist and overpower him\n"
            p.allowed_resps = ["throw it", "attempt to grapple"]
    elif answer == "second":
            delay_print("You open the second door to a dimly lit room and hear maniacal laughter\n")
            delay_print("You walk in and immiedately slip on a wet surface falling on your back\n")
            delay_print("As you open your eyes with stars in your vision you see a goblin above you with a rock\n")
            delay_print("He brings the rock down and your vision goes dark as you hear 'Gobby did good, capture hostage, Gobby gets treat'\n")
            startoverAction(answer)
    elif answer == "third":
        if "regular clothes" not in p.inventory:
            delay_print("You open the third door to see a lady who screams and immediately throws a small object that hits you in the temple\n")
            delay_print("Your vision starts to blur and the lady charges you striking you across the head, your vision goes dark as you crumple to the floor\n")
            startoverAction(answer)
        else:
            if "regular clothes" in p.inventory:
                delay_print("You open the third door to see a lady sitting in front of a vanity mirror brushing her hair\n")
                delay_print("'Well hello there, I see you managed to escape your room, would you like to help me with something?\n")
                p.location = "thirdroom"
                p.prompt = "Do you help the lady or no?\n"
                p.allowed_resps = ["yes", "no"]

def thirdroomAction(answer):
    if answer == "yes":
        delay_print("'Wonderful, I haven't had any visitors in awhile and really need help rearranging this room\n")
        delay_print("You see her stand up and start moving almost as if floating around the room telling you where to move things\n")
        dieroll = random.randint(1,20)
        cprint(dieroll, "magenta")
        if dieroll >= 12:
            delay_print("You move the furniture around easily and she is beaming with happiness at her rearranged room\n")
            delay_print("'Here take this as a token of gratitude'")
            delay_print("She hands you a small object that as it comes in contact with your hand instantly transforms into small bracers with intricate designs\n")
            delay_print("When you look back to thank the lady she is gone\n")
            if "bracers" not in p.inventory:
                p.inventory.append("bracers")
                cprint(f"Inventory:{p.inventory}", "green")
                p.armor = p.armor + 2
                cprint(f"Armor:{p.armor}", "cyan")
            else:
                delay_print("")
                p.location = "emptyroom"
                p.prompt = "What would you like to do next?\n"
                p.allowed_resps = ["look around", "check the furniture", "back"] 
        else:
            delay_print("As you start to move things you accidently tip the vanity over shattering the mirror\n")
            delay_print("You hear a shriek that pierces your mind causing you to drop to one knee in pain as you cover your ears\n")
            p.health = p.health - 5
            cprint(f"HP:{p.health}", "red")
            delay_print("The shriek clears almost as fast as it came, as you stand up and look around the lady is no where to be seen\n")
            p.location = "emptyroom"
            p.prompt = "What would you like to do next?\n"
            p.allowed_resps = ["look around", "check the furniture", "back"]
    if answer == "no":
        delay_print("'Oh that is a shame, Why would you barge into my room then not offer to help?\n")
        delay_print("As the last of her words leave her mouth you hear a high pitched shriek causing you to drop to your knees and cover your ears\n")
        p.health = p.health - 5
        cprint(f"HP:{p.health}", "red")
        delay_print("When you stand up the lady is no where to be seen\n")
        p.location = "emptyroom"
        p.prompt = "What would you like to do next?\n"
        p.allowed_resps = ["look around", "check the furniture", "back"]




def firstroomAction(answer):
    if answer == "throw it":
        p.inventory = pydash.without(p.inventory, "mystery vial")
        cprint(f"Inventory:{p.inventory}", "green")
        dieroll = random.randint(1,20) + 3
        cprint(dieroll, "blue")
        if dieroll >= 15:
            delay_print("You hit the cultist in the face and the vial shatters causing him to fall unconcious\n")
            p.location = "emptyroom"
            p.prompt = "What do you want to do now?\n"
            p.allowed_resps = ["loot cultist","look around","back"]
        else:
            delay_print("The vial sails by the cultist because of your bad aim, and he laughs at you then charges\n")
            delay_print("You attempt to grapple him and take him out by hand\n")
            dieroll = random.randint(1,20) + 1
            cprint(dieroll, "blue")
            if dieroll >=12:
                delay_print("You catch him off guard as he charges you and manage to knock him out by tripping him\n")
                p.location = "emptyroom"
                p.prompt = "What would you like to do now?"
                p.allowed_resps = ["loot cultist","look around","back"]
            else:
                delay_print("The guard charging you catches you by surprise and you stumble backwards\n")
                delay_print("because you are off balance he is able to bring his club up and catch you in the temple\n")
                startoverAction(answer)
    if answer == "attempt to grapple":
        dieroll1 = random.randint(1,20)
        dieroll2 = random.randint(1,20)
        cprint(dieroll1, "blue")
        cprint(dieroll2, "yellow")
        while dieroll1 == dieroll2:
            dieroll1 = random.randint(1,20)
            cprint(dieroll1, "blue")
            dieroll2 = random.randint(1,20)
            cprint(dieroll2, "yellow")
        if dieroll1 > dieroll2:
            delay_print("You manage to subdue the cultist and knock him unconcious\n")
            p.location = "emptyroom"
            p.prompt = "What would you like to do now?"
            p.allowed_resps = ["loot cultist","look around","back"]
        if dieroll1 < dieroll2:
            delay_print(" The cultist charges you and easily overpowers you bringing his club down over your head")
            startoverAction(answer)
    if answer == "draw sword":
        dieroll = random.randint(1,20) + 2
        cprint(dieroll1, "blue")
        if dieroll > 14:
            delay_print("You manage to draw your sword and catch the cultist off guard, your blade slices across his neck as blood sprays out\n")
            p.location = "emptyroom"
            p.prompt = "What would you like to do now?"
            p.allowed_resps = ["loot cultist","look around","back"]
        else:
            delay_print("You didn't react fast enough and the cultist closes the distance quickly bringing his club up ready to fight\n")
            dieroll1 = random.randint(1,20) + 2
            dieroll2 = random.randint(1,20) + 3
            if dieroll1 < dieroll2:
                delay_print("You draw your sword using your hilt you catch him in the stomach then bring your sword down removing his head\n")
            if dieroll1 > dieroll2:
                delay_print("He brings his club up and connects with your shoulder\n")
                p.health = p.health - 5
                cprint(f"HP:{p.health}", "red")
                delay_print("You bring your sword up and catch his stomach, slicing it open and causing the contents to spill on the ground\n")
                p.location = "emptyroom"
                p.prompt = "What would you like to do now?"
                p.allowed_resps = ["loot cultist","look around","back"]

def emptyroomAction(answer):
    if answer == "loot cultist":
        if "Sword" not in p.inventory:  
            p.inventory.append("Sword")
            cprint(f"Inventory:{p.inventory}", "green")
            delay_print("You find a small sword on the cultist that you can use, remember you can only wield one weapon and shield at a time\n")
    if answer == "look around":
        delay_print("You see a door leading to the second room, or a door going forward\n")
        p.location = "emptyroom"
        p.prompt = "What would you like to do?\n"
        p.allowed_resps = ["open the door in front", "go to second room", "back"]
    if answer == "go to second room":
        if "Sword" not in p.inventory:
            delay_print("You open the second door to a dimly lit room and hear maniacal laughter\n")
            delay_print("You walk in and trip on a hidden wire hitting your head on the cobblestone floor\n")
            delay_print("As you open your eyes with stars in your vision you see a goblin above you with a rock\n")
            delay_print("He brings the rock down and your vision goes dark as you hear 'Gobby did good, capture hostage, Gobby gets treat'\n")
            startoverAction(answer)
        if "Sword" in p.inventory:
            delay_print("You open the second door to a dimly lit room and hear maniacal laughter\n")
            delay_print("You walk in and trip on a hidden wire hitting your head on the cobblestone floor\n")
            delay_print("As you open your eyes with stars in your vision you see a goblin above you with a rock\n")
            delay_print("Thinking quickly you draw the sword you just got and manage to bury it to the hilt just under the goblins chin.\n")
            delay_print("You stand up and pull the sword out of the goblin and clean the blood off resheathing it\n")
            p.location = "secondroom"
            p.prompt = "What would you like to do?\n"
            p.allowed_resps = ["look around", "loot goblin"]
    if answer == "open the door in front":
        delay_print("You open the door and get slightly blinded by a bright light\n")
        delay_print("As your eyes adjust you make out that you are in a courtyard, where you see a wagon, a gate leading outside, and a door on the building you just came out of\n")
        delay_print("You notice that the door you just came through is no longer there and you get a bad feeling that this place is not normal\n")
        p.location = "courtyard"
        p.prompt = "What would you like to do?\n"
        p.allowed_resps = ["wagon","gate","door"]
    if answer == "check the furniture":
        dieroll = random.randint(1,20)
        cprint(dieroll, "magenta")
        if dieroll <=8:
            delay_print("You search the different pieces of furniture and find a few coins and valuables\n")
            if "gold pieces" not in p.inventory:
                p.inventory.append("gold pieces")
                cprint(f"Inventory:{p.inventory}", "green")
            delay_print("You look around and see a door going forward and a door going to the second room\n")
            p.location = "emptyroom"
            p.prompt = "What would you like to do?\n"
            p.allowed_resps = ["open the door in front", "go to second room"]
        else:
            delay_print("As you approach a piece of furniture, it transforms magically growing teeth and a tongue shoots out grabbing you and pulling you towards it\n")
            delay_print("You struggle as much as you can but to no avail, you are swallowed by this piece of furniture with teeth\n")
            startoverAction(answer)
    if answer == "back":
        delay_print("You head back out of the room you are in but feel a strange presence come over you\n")
        delay_print("You come back out to the room with three doors\n")
        p.location = "threedoor"
        p.prompt = "Which door do you choose to go into?\n "
        p.allowed_resps = ["first", "second", "third","back"]
    if answer == "hatch":
        delay_print("You go to the hatch and hear running water behind the doors, you also catch a faint smell as you get close\n")
        p.location = "hatch"
        p.prompt = "Do you open the hatch?"
        p.allowed_resps = ["yes", "no"]
    if answer == "first":
        if "mystery vial" or "sword" not in p.inventory:
            delay_print("You open the door and find an armored cultist that turns upon hearing the door open\n")
            delay_print("he shouts, 'Hey, How did you get out!' he draws his club and hits you over the head\n")
            delay_print("You see stars and your vision dims as you fall over from the blow\n")
            startoverAction(answer)
        if "mystery vial" in p.inventory:
            delay_print("You open the door and find an armored cultist that turns upon hearing the door open\n")
            delay_print("You are surprised to see the cultist has been revived but you react fast\n")
            p.location = "firstroom"
            p.prompt = "Do you throw the vial, or attempt to grapple him\n"
            p.allowed_resps = ["throw it", "attempt to grapple",]
        else:
            "sword" in p.inventory
            delay_print("You open the door and find an armored cultist that turns upon hearing the door open\n")
            delay_print("You are surprised to see the cultist has been revived but you react fast\n")
            p.location = "firstroom"
            p.prompt = "Do you draw your sword, or attempt to grapple him\n"
            p.allowed_resps = ["draw sword", "attempt to grapple"]

    elif answer == "second":
            delay_print("You open the second door to a dimly lit room and hear maniacal laughter\n")
            delay_print("You walk in and immiedately slip on a wet surface falling on your back\n")
            delay_print("As you open your eyes with stars in your vision you see a goblin above you with a rock\n")
            delay_print("He brings the rock down and your vision goes dark as you hear 'Gobby did good, capture hostage, Gobby gets treat'\n")
            startoverAction(answer)
    elif answer == "third":
        if "regular clothes" not in p.inventory:
            delay_print("You open the third door to see a lady who screams and immediately throws a small object that hits you in the temple\n")
            delay_print("Your vision starts to blur and the lady charges you striking you across the head, your vision goes dark as you crumple to the floor\n")
            startoverAction(answer)
        else:
            if "regular clothes" in p.inventory:
                delay_print("You open the third door to see a lady sitting in front of a vanity mirror brushing her hair\n")
                delay_print("'Well hello there, I see you managed to escape your room, would you like to help me with something?\n")
                p.location = "thirdroom"
                p.prompt = "Do you help the lady or no?\n"
                p.allowed_resps = ["yes", "no"]


def secondroomAction(answer):
    if answer == "look around":
        delay_print("You check your surroundings and see this must be a bedroom for a goblin, it has alot of bones strewn around and crude furniture\n")
        delay_print("You also see a hatch in the back of the room, as well as three doors that lead out to the other rooms you can enter\n")
        p.location = "emptyroom"
        p.prompt = "What would you like to do?\n"
        p.allowed_resps = ["hatch", "back", "third", "first"]
    if answer == "loot goblin":
        delay_print("You look over the goblin and find a necklace with a ring\n")
        if "gold ring" not in p.inventory:
            p.inventory.append("gold ring")
            cprint(f"Inventory:{p.inventory}","green")
        delay_print("As you put the ring on you are flooded with images\n")
        delay_print("You start to remember that you are a Cleric with the Order of the Gauntlet\n")
        delay_print("You recover from the onslaught on images and look around\n")
        delay_print("You check your surroundings and see this must be a bedroom for a goblin, it has alot of bones strewn around and crude furniture\n")
        delay_print("You also see a hatch in the back of the room, as well as three doors that lead out to the other rooms you can enter\n")
        p.location = "emptyroom"
        p.prompt = "What would you like to do?\n"
        p.allowed_resps = ["hatch", "back", "third", "first"]
    

def hatchAction(answer):
    if answer == "yes":
        delay_print("You open the hatch in the back of the room to see a small river\n")
        delay_print("Seconds after you open the hatch you get hit with a foul smell\n")
        p.location = "hatch"
        p.prompt = "Do you go down through the hatch?\n"
        p.allowed_resps = ["drop down","Close the door"]
    if answer == "no":
        delay_print("You decide the smell is to bad and don't open the hatch door\n")
        p.location = "emptyroom"
        p.prompt = "What are you going to do now?\n"
        p.allowed_resps = ["hatch", "back", "third", "first"]
    if answer == "Drop down":
        delay_print("You drop down into the running water making a small splash\n")
        delay_print("You see two paths, one up river and one down river\n")
        p.location = "hatch"
        p.prompt = "Which path do you choose\n"
        p.allowed_resps = ["up river","down river", "back"]
    if answer == "Close the door":
        delay_print("You decide the smell is to bad and close the hatch door\n")
        p.location = "emptyroom"
        p.prompt = "What are you going to do now?\n"
        p.allowed_resps = ["hatch", "back", "third", "first"]
    if answer == "up river":
        delay_print("You start to wade up river against the current, its very slippery but you keep going\n")
        dieroll = random.randint(1,20)
        cprint(dieroll, "blue")
        if dieroll >=15:
            delay_print("You manage to get up to a small room where the river is coming from.\n")
            delay_print("There is a small pond in the middle of the room, but other then that there is nothing special about the room\n")
            p.location = "lakeroom"
            p.prompt = "What would you like to do?\n"
            p.allowed_resps = ["go back", "look around", "wade into the lake"]
        else:
            delay_print("As you are wading up the river you lose your footing and the current carries you back down river\n")
            delay_print("You stand up now soaked to the bone\n")
            p.health = p.health - 5
            cprint(f"hp:{p.health}","red")
            p.location = "hatch"
            p.prompt = "Which path do you choose\n"
            p.allowed_resps = ["up river","down river", "back"]
    if answer == "down river":
        delay_print("You follow the current but as you follow it the stench becomes worse burning your nostrils with a putrid smell\n")
        delay_print("Just as you think it can't get any worse you come upon a small grated door that looks to open in a large room\n")
        delay_print("In this room you see a circle drawn with what looks like blood and candles surrounding it, with some bones in the middle\n")
        p.location = "sacrificeroom"
        p.prompt = "What would you like to do?\n"
        p.allowed_resps = ["open the door", "head back up river"]
    if answer == "back":
        delay_print("After seeing what is down here you decide not to push any farther and crawl back out of the hatch")
        p.location = "emptyroom"
        p.prompt = "What would you like to do?\n"
        p.allowed_resps = ["hatch", "back", "third", "first"]

#def lakeroomAction(answer):
    

def sacrificeroomAction(answer):
    if answer == "Open the door":
        delay_print("You push the door open making a loud screeching sound that is echoing through the room\n")
        delay_print("You hear a scuffling sounds but can't pinpoint where they are coming from due to the echoes\n")
        delay_print("The room goes cold as a shadow moves into view, a sound that is akin to nails on a chalkboard eminates from the shadow\n")
        delay_print("'Gobby Issssss that you? What are you doing down here again' the shadow moves around the room 'Master will be upset with you if you are caught outside your room again'\n")
        p.location = "sacrificeroom"
        p.prompt = "You can try to fool the Spectre, attempt to fight it, or run, which do you do?\n"
        p.allowed_resps = ["fool it", "fight it", "run"]
    if answer == "head back up river":
        delay_print("You get an ominous feeling from the room and decide to turn back around\n")
        p.location = "hatch"
        p.prompt = "Which path do you choose\n"
        p.allowed_resps = ["up river","down river", "back"]
    if answer == "Fool it":
        dieroll = random.randint(1,20)
        cprint(dieroll, "blue")
        if dieroll >=8:
            delay_print("'I am looking for my lost possesions, where did you put them hmm?' you attempt your best impersonation of a goblins voice")
            delay_print("The spectre pauses for a second before responding 'Well I was going to return it soon, the",print(p.race),"had interesting things' You see the spectre motion over into the corner and you see a pile of items\n")
            p.location = "sacrificeroom"
            p.prompt = "What would you like to do?\n"
            p.allowed_resps = ["go to pile", "try to sneak attack", "run"]
        else:
            delay_print("You try your best impression of a goblin but the spectre immediately knows you are not who you are saying\n")
            delay_print("The Spectre starts to move towards you slowly rearing up ready to fight\n")
            p.location = "sacrificeroom"
            p.prompt = "What is your next move?\n"
            p.allowed_resps = ["fight it", "run"]
    if answer == "fight it":
        if "holy sword" in p.inventory or "excalibur" in p.inventory:
            dieroll = random.randint(1,20) + 4
            cprint(dieroll, "blue")
            if dieroll > 14:
                delay_print("You draw your sword and swing at the spectre, cutting a section of the darkness out and causing it to shriek and run\n")
            else:
                delay_print("You draw your sword and swing at the spectre, you fall off balance as you swing missing the spectre\n")
                delay_print("The spectre rears back shrieking as a black arm swipes out at you\n")
                dieroll2 = random.randint(1,20) + 3
                if dieroll2 <= p.armor:
                    delay_print("You manage to dodge the arm and prepare for another attack but the spectre is now gone")
                else:
                    delay_print("Because you are off balance you can't avoid the attack and it catches you on your shoulder\n")
                    delay_print("You stand up blood dripping down your arm to continue the fight only to find yourself alone\n")
                    p.health = p.health - 3
                    cprint(f"HP:{p.health}", "red")
            p.location = "sacrificeroom"
            p.prompt = "What would you like to do now?\n"
            p.allowed_resps = ["look around", "back"]
        else:
            delay_print("You draw your sword and swing but the blade goes right through the darkness not hitting anything\n")
            delay_print("You then hear the spectre laughing as the darkness envelops you 'Another Soul to torture for eternity'\n")
            startoverAction(answer)
    if answer == "run":
            delay_print("You turn and quietly sneak back through the door, going back up to the hatch\n")
            p.location = "hatch"
            p.prompt = "Which path do you choose\n"
            p.allowed_resps = ["up river","down river", "back"]
    if answer == "look around":
        delay_print("With the spectre gone you see a pile of items over in the corner and something shiny is glinting in the low light\n")
        delay_print("You also see a door that seems about the same size of the spectre you assume that is where it went\n")
        p.location = "sacrificeroom"
        p.prompt = "What is your next move?\n"
        p.allowed_resps = ["go to pile", "go to door", "back"]
    if answer == "go to pile":
        delay_print("You walk over to the pile of items and sift through it, you find a health potion and a shield\n")
        delay_print("You pick up the shield and notice a helmet that looks very familiar like a long lost memory\n")
        delay_print("You notice while holding the shield you feel a surge of energy revitilizing you\n")
        if "hpotion" not in p.inventory:
            p.inventory.append("hpotion")
            cprint(f"Inventory:{p.inventory}", "green")
        p.location = "sacrificeroom"
        p.prompt = "Do you keep the shield and the helmet?\n"
        p.allowed_resps = ["keep them", "throw them back in the pile"]
    if answer == "keep them":
        if "shield" not in p.inventory:
            p.inventory.append("shield")
            cprint(f"Inventory:{p.inventory}", "green")
            delay_print("You slip the shield on your back taking in the feeling of being revitilized\n")
        else:
            delay_print("You try to put the shield on your back and it teleports back to the pile, you realise that you cannot carry two shields at once\n")
        if "helmet" not in p.inventory:
            p.inventory.append("helmet")
            cprint(f"Inventory:{p.inventory}", "green")
            delay_print("As you slip the helmet on more of your memories start coming back, you are greeted by images of a large kingdom far away, a high temple that bears the same mark as your helmet\n")
        else:
            delay_print("You go to put the helmet on but then realize you can't exactly put a second helmet on so you throw it back in the pile, slightly concerned there are two helmets that are extremely familiar to you.\n")
    if answer == "throw them back in the pile":
        delay_print("The shield and helmet just don't feel right ")
    if answer == "try to sneak attack":
        if "holy sword" in p.inventory or "excalibur" in p.inventory:
            dieroll = random.randint(1,20) + 4
            cprint(dieroll, "blue")
            if dieroll > 14:
                delay_print("You draw your sword and swing at the spectre, cutting a section of the darkness out and causing it to shriek and run\n")
            else:
                delay_print("You draw your sword and swing at the spectre, you fall off balance as you swing missing the spectre\n")
                delay_print("The spectre rears back shrieking as a black arm swipes out at you\n")
                dieroll2 = random.randint(1,20) + 3
                if dieroll2 <= p.armor:
                    delay_print("You manage to dodge the arm and prepare for another attack but the spectre is now gone")
                else:
                    delay_print("Because you are off balance you can't avoid the attack and it catches you on your shoulder\n")
                    delay_print("You stand up blood dripping down your arm to continue the fight only to find yourself alone\n")
                    p.health = p.health - 3
                    cprint(f"HP:{p.health}", "red")
            p.location = "sacrificeroom"
            p.prompt = "What would you like to do now?\n"
            p.allowed_resps = ["look around", "back"]
    if answer == "go to door":
        delay_print("You walk up to the door and get an uneasy feeling as you get closer to the door, you feel that the shade has retreated through this door\n")
        p.location = "sacrificedoor"
        p.prompt = "What would you like to do?\n"
        p.allowed_resps = ["Open the door", "kick the door down", "leave"]

def sacrificedoorAction(answer):
    if answer == "Open the door":
        delay_print("As you grab the door handle a searing pain runs through your arm and it instantly feels like you just dipped your arm in ice water up to your shoulder\n")
        p.health = p.health - 1
        cprint(f"HP:{p.health}", "red")
        p.location = "sacrificedoor"
        p.location = "What would you like to do now?\n"
        p.allowed_resps = ["Open the door", "kick the door down", "leave"]
    if answer == "kick the door down":
        dieroll = random.randint(1,20) + p.stremod
        if dieroll >= 14:
            delay_print("As you foot connects with the door it swings in with a loud bang revealing a small room where the shade is no where to be seen but you see a creature with a face of tentacles\n")
            delay_print("The creature turns to you and greats you almost as if speaking in your head\n")
            delay_print("Welcome great traveler I see you survived my illusion, what is it you desire so greatly that you have intruded on my home?\n")
         



    

def courtyardAction(answer):
    if answer == "wagon":
        if "bracers" not in p.inventory:
            delay_print("As you start to move, you see movement on the walls surrounding the courtyard\n")
            delay_print("Suddenly the movement on the walls stop and hundreds of archers appear with their bows drawn taught aimed directly at you\n")
            delay_print("One of the archers, who you assume to be the captain, speaks out 'You shouldn't be here, you will pay for breaking the law'\n")
            delay_print("A single archer looses his arrow, you raise your hand to try and stop it, but suddenly it sprouts from your leg\n")
            delay_print("You feel your muscles quickly lock up and the world goes dark\n")
            startoverAction(answer)
        if "bracers" in p.inventory:
                delay_print("As you start to move, you see movement on the walls surrounding the courtyard\n")
                delay_print("Suddenly the movement on the walls stop and hundreds of archers appear with their bows drawn taught aimed directly at you\n")
                delay_print("One of the archers, who you assume to be the captain, speaks out 'You shouldn't be here, you will pay for breaking the law'\n")
                delay_print("A single archer looses his arrow, you raise your hand to try and stop it, Suddenly what looks like a blue curtain appears in front of you\n")
                delay_print("The arrow stops midair, caught by this new curtain.  The captain shouts the command to fire and you see hundreds of arrows appear stopped in a simliar manner to the first arrow\n")
                delay_print("The bracers start to glow a bright blue and suddenly all of the arrows are returned at high speed back to the archer that fired it and you hear the bodies thudding to the ground\n")
                delay_print("You feel worn out suddenly but drag yourself over to the wagon")
                p.location = "courtyard2"
                p.prompt = "What would you like to do now?"
                p.allowed_resps = ["search wagon", "rest", "go to door", "go to gate"]
    if answer == "gate":
        if "bracers" not in p.inventory:
            delay_print("As you start to move, you see movement on the walls surrounding the courtyard\n")
            delay_print("Suddenly the movement on the walls stop and hundreds of archers appear with their bows drawn taught aimed directly at you\n")
            delay_print("One of the archers, who you assume to be the captain, speaks out 'You shouldn't be here, you will pay for breaking the law'\n")
            delay_print("A single archer looses his arrow, you raise your hand to try and stop it, but suddenly it sprouts from your leg\n")
            delay_print("You feel your muscles quickly lock up and the world goes dark\n")
            startoverAction(answer)
        if "bracers" in p.inventory:
            delay_print("As you start to move, you see movement on the walls surrounding the courtyard\n")
            delay_print("Suddenly the movement on the walls stop and hundreds of archers appear with their bows drawn taught aimed directly at you\n")
            delay_print("One of the archers, who you assume to be the captain, speaks out 'You shouldn't be here, you will pay for breaking the law'\n")
            delay_print("A single archer looses his arrow, you raise your hand to try and stop it, Suddenly what looks like a blue curtain appears in front of you\n")
            delay_print("The arrow stops midair, caught by this new curtain.  The captain shouts the command to fire and you see hundreds of arrows appear stopped in a simliar manner to the first arrow\n")
            delay_print("The bracers start to glow a bright blue and suddenly all of the arrows are returned at high speed back to the archer that fired it and you hear the bodies thudding to the ground\n")
            delay_print("You feel worn out suddenly but wearily make your way to the gate")
            p.location = "courtyard2"
            p.prompt = "What would you like to do now?"
            p.allowed_resps = ["open the gate", "rest", "go to door", "go to wagon"]
    if answer == "door":
        delay_print("As you start to move, you see movement on the walls surrounding the courtyard\n")
        delay_print("Suddenly the movement on the walls stop and hundreds of archers appear with their bows drawn taught aimed directly at you\n")
        delay_print("One of the archers, who you assume to be the captain, speaks out 'You shouldn't be here, you will pay for breaking the law'\n")
        if "bracers" not in p.inventory:
            dieroll = random.randint(1,20) - 4
            cprint(dieroll,"yellow")
            if dieroll <= p.armor:
                delay_print("You start sprinting towards the door and manage to open it and get inside as you hear two thuds of an arrow embed in the door\n")
                delay_print("You look around and realise somehow you are back in the original room and the door you just came through magically vanished again\n")
                p.location = "darkroom2"
                p.prompt = "What would you like to do?"
                p.allowed_resps = ["window", "explore", "chest", "pile of clothes"]
            else:
                delay_print("You start sprinting towards the door but suddenly an agonizing pain runs up your leg, you look down to see an arrow in your calf\n")
                delay_print("You feel your muscles quickly lock up and the world goes dark\n")
                startoverAction(answer)
        if "bracers" in p.inventory:
            dieroll = random.randint(1,20) + 4
            cprint(dieroll, "yellow")
            if dieroll <= p.armor:
                delay_print("You start sprinting towards the door and manage to open it and get inside as you hear two thuds of an arrow embed in the door\n")
                delay_print("You look around and realise somehow you are back in the original room and the door you just came through magically vanished again\n")
                p.location = "darkroom2"
                p.prompt = "What would you like to do?"
                p.allowed_resps = ["Window", "explore", "chest", "pile of clothes"]
            else:
                delay_print("You start sprinting towards the door but suddenly an agonizing pain runs up your leg, you look down to see an arrow in your calf\n")
                delay_print("You feel your muscles quickly lock up and the world goes dark\n")
                startoverAction(answer)





def atwindowAction(answer):
    if answer == "break it":
        dieroll = random.randint(1,20)
        cprint(dieroll, "magenta")
        if dieroll >= 16:
            delay_print("The window breaks and you fall out into an empty courtyard\n")
            delay_print("You look around and see a wagon, a gate, and a door back into the building you just fell out of \n")
            p.health = p.health - 10
            cprint(f"hp:{p.health}","red")
            p.location = "courtyard"
            p.prompt = "Do you check the wagon, go to the gate, or check the door "
            p.allowed_resps = ["wagon","gate","door"]
        else:
            delay_print("You hear the window crack a bit. ")
    elif answer == "open door":
        dieroll = random.randint(1,20)
        cprint(dieroll, "magenta")
        if dieroll >= 14:
            delay_print("You have sucessfully opened the door!\n")
            delay_print("You step out of the room onto a landing with a staircase going up, and one going down \n")
            p.location = "landing"
            p.prompt = "Do you go up or down the stairs?\n"
            p.allowed_resps = ["up","down"]
        else:
            delay_print("The door is wedged but you feel it give a bit\n")

def racechoiceAction(answer):
    p.race = answer
    cprint(f"You chose the race {p.race} as your race", "red")
    p.location = "genderchoice"
    p.prompt = "what is your Gender?\n"
    p.allowed_resps = ["male", "female"]

def genderchoiceAction(answer):
    p.gender = answer
    cprint(f"You chose to be {p.gender} as your gender", "red")

    delay_print("You awake in a dark room, You don't remember where you are or how you got there.\n")
    delay_print("You look around and see a pile of clothes, a chest, and a window.\n")
    p.location = "darkroom"
    p.prompt = "Do you check the pile of clothes, the chest, the window?\n"
    p.allowed_resps = ["pile of clothes", "chest", "window"]

def vialAction(answer):
    if answer == "yes":
        print("You become drowsy and stumble around falling into bed and the world goes black\n")
        startoverAction(answer)
    elif answer == "no":
            if "mystery vial" not in p.inventory:
                delay_print("You put the vial in your pocket to save it for later\n")
                p.inventory.append("mystery vial")
                cprint(f"Inventory:{p.inventory}", "green")
            else:
                delay_print("As you go to put the vial in your pocket it crumbles to dust and disappears\n")
            delay_print("You now need to decide what to do. \n")
            p.location = "darkroom"
            p.prompt = "Do you go to the window or check the pile of clothes\n"
            p.allowed_resps = ["window","pile of clothes"]


def action(answer):
    if answer == "stats":
        cprint(f"Strength:{p.strength}", "cyan") 
        cprint(f"Intelligence:{p.intelligence}", "cyan") 
        cprint(f"Charisma:{p.charisma}", "cyan")
        cprint(f"Constitution:{p.constitution}","cyan")
        cprint(f"Wisdom:{p.wisdom}", "cyan")
        cprint(f"Dexterity:{p.dexterity}", "cyan")
        cprint(f"Armor Class:{p.armor}", "cyan")
    if answer == "mods":
        cprint(f"Strength:{p.strmod}", "cyan")
    if answer == "gender":
        cprint(f"You are a {p.gender}")
    if answer == "inv":
        cprint(f"Inventory:{p.inventory}", "green")
    if answer == "hpotion":
        if "hpotion" in p.inventory:
            p.health = min(p.health + 10, p.maxhp)
            p.inventory = pydash.without(p.inventory, "hpotion")
        else:
            delay_print("You don't have a health potion.")
        cprint(f"HP:{p.health}", "red")
    if answer == "health":
        cprint(f"HP:{p.health}", "red")
    if p.location == "racechoice":
        racechoiceAction(answer)
    elif p.location == "genderchoice":
        genderchoiceAction(answer)
    elif p.location == "darkroom":
        darkroomAction(answer)
    elif p.location == "darkroom2":
        darkroom2Action(answer)
    elif p.location == "walkingroom":
        opendoorAction(answer)
    elif p.location == "sacrificeroom":
        sacrificeroomAction(answer)
    elif p.location =="atwindow":
        atwindowAction(answer)
    elif p.location == "roomwithvial":
        vialAction(answer)
    elif p.location == "landing":
        landingAction(answer)
    elif p.location == "triplehall":
        triplehallAction(answer)
    elif p.location == "losthall":
        losthallAction(answer)
    elif p.location == "courtyard":
        courtyardAction(answer)
    elif p.location == "threedoor":
        threedoorAction(answer)
    elif p.location == "firstroom":
        firstroomAction(answer)
    elif p.location == "secondroom":
        secondroomAction(answer)
    elif p.location == "thirdroom":
        thirdroomAction(answer)
    elif p.location == "emptyroom":
        emptyroomAction(answer)
    elif p.location == "sacrificedoor":
        sacrificedoorAction(answer)
    elif p.location == "hatch":
        hatchAction(answer)
    else:
        raise NotImplementedError() 


class Player:
    location = "racechoice"
    prompt = "What is the race of your character?\n"
    allowed_resps: "list[str]"
    inventory: "list[str]" = []
    always_resps = ["inv", "health", "hpotion", "stats", "mods", "gender"]
    race: "str | None"
    gender: 'Literal["male", "female", None]'
    health = 30
    _base_max_hp = 30
    armor = 10
    _strength = 10
    _intelligence = 10
    _charisma = 10
    _constitution = 10
    _wisdom = 10
    _dexterity = 10
    strmod: int
    
    @property
    def maxhp(self) -> int:
        bonuses = 0
        if "shield" in self.inventory:
            bonuses += 5
        if "something else" in self.inventory:
            bonuses += 3
        return self._base_max_hp + bonuses
    @property
    def strength(self) -> int:
        bonus = 0
        if self.race == "human": 
            bonus += 0
        elif self.race == "dragonborn":
            bonus += 2
        elif self.race == "elf":
            bonus += 1
        elif self.race == "dwarf":
            bonus += 3
        elif self.race == "tiefling":
            bonus += -1
        elif self.race == "halfling":
            bonus += -2
        elif self.race == "orc":
            bonus += 3
        return self._strength + bonus
    @property
    def intelligence(self) -> int:
        bonus = 0
        if self.race == "human":
            bonus += 1
        elif self.race == "dragonborn":
            bonus += 1
        elif self.race == "elf":
            bonus += 3
        elif self.race == "dwarf":
            bonus += 0
        elif self.race == "tiefling":
            bonus += 2
        elif self.race == "halfling":
            bonus += 1
        elif self.race == "orc":
            bonus += -2
        return self._intelligence + bonus
    @property
    def charisma(self) -> int:
        bonus = 0
        if self.race == "human":
            bonus += 1
        elif self.race == "dragonborn":
            bonus += -1
        elif self.race == "elf":
            bonus += 3
        elif self.race == "dwarf":
            bonus += -2
        elif self.race == "tiefling":
            bonus += -1
        elif self.race == "halfling":
            bonus += 1
        elif self.race == "orc":
            bonus += -3
        return self._charisma + bonus
    @property
    def constitution(self) -> int:
        bonus = 0
        if self.race == "human":
            bonus += 0
        elif self.race == "dragonborn":
            bonus += 1
        elif self.race == "elf":
            bonus += -1
        elif self.race == "dwarf":
            bonus += 3
        elif self.race == "tiefling":
            bonus += -1
        elif self.race == "halfling":
            bonus += -1
        elif self.race == "orc":
            bonus += 3
        return self._constitution + bonus
    @property
    def wisdom(self) -> int:
        bonus = 0
        if self.race == "human":
            bonus += -1
        elif self.race == "dragonborn":
            bonus += 0
        elif self.race == "elf":
            bonus += 1
        elif self.race == "dwarf":
            bonus += 1
        elif self.race == "tiefling":
            bonus += -1
        elif self.race == "halfling":
            bonus += -1
        elif self.race == "orc":
            bonus += -1
        return self._wisdom + bonus
    @property
    def dexterity(self) -> int:
        bonus = 0
        if self.race == "human":
            bonus += 3
        elif self.race == "dragonborn":
            bonus += 0
        elif self.race == "elf":
            bonus += 2
        elif self.race == "dwarf":
            bonus += 1
        elif self.race == "tiefling":
            bonus += 1
        elif self.race == "halfling":
            bonus += 3
        elif self.race == "orc":
            bonus += 0
        return self._dexterity + bonus
    @property
    def strmod(self) -> int:
        return (self._strength - 10) // 2
    @property
    def intemod(self) -> int:
        return (self._intelligence - 10) // 2
    @property
    def chamod(self) -> int:
        return (self._charisma - 10) // 2
    @property
    def dexmod(self) -> int:
        return (self._dexterity - 10) // 2
    @property
    def conmod(self) -> int:
        return (self._constitution - 10) // 2
    @property
    def wismod(self) -> int:
        return (self._wisdom - 10) // 2

    


#def unit_test():
#    testing_player = Player()
#    assert testing_player.maxhp == 30
#    testing_player.inventory.append("something else")
#    assert testing_player.maxhp == 33
#    testing_player.inventory.append("shield")
#    assert testing_player.maxhp == 38
#    testing_player.inventory = pydash.without(testing_player.inventory, "something else")
#    assert testing_player.maxhp == 35

#unit_test()

delay_print("You are about to play my game, at any time you are prompted you can check your health or your inventory with the words health or inv\n")
delay_print("Be warned though, This is a game of thinking, trying different things with items in your inventory may reveal different results\n")
delay_print("You will see different colors numbers, they correspond to different actions\n")
delay_print("Magenta = skill check, blue= you attacking something, yellow=an attack made against you\n")
delay_print("Good luck and may the odds be in your favor\n")

delay_print("You will set up your character first, then start your journey\n")

p = Player()
p.prompt = "What is the race of your character?\n"
p.allowed_resps = ["human", "dragonborn", "dwarf", "tiefling", "halfing", "elf", "orc"]

# Forever: ask the user for input
while True:
    answer = inputFromList(
        p.prompt,
        p.allowed_resps + p.always_resps
    )
    action(answer)
    if p.health <= 0:
        startoverAction(answer)
    
