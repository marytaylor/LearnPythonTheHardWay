#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

inventory = ['gum']

def start():
    print "Your arms are tied behind you."
    print "What do you do now?"

    decide1 = raw_input("> ")

    if decide1 == "scream":
        scream()

    elif "feel" in decide1:
        print "Theres something that feels like a hook on the wall behind your back."
        decide4 = raw_input("> ")
        if "pull" or "tag" or "grab" or "grasp" in decide4:
            # this seems to run no matter what I input here
            print "The wall above you opens and you realize you were in the trunk of a car."
            print "As you look around you see several vehicles; you must be in a parking garage."
            escape()
        elif "pocket" in decide4:
            gum()
            decide5 = raw_input("> ")
        else:
            nothing()
            start()
    elif "inventory" in decide1:
        inventory()
        start()
    else:
        nothing()
        start()

def nothing():
    print "Nothing happens"

def scream():
    nothing()
    print "What now?"
    decide2 = raw_input("> ")
    if decide2 == "scream":
        nothing()
        print "What now?"
        decide3 = raw_input("> ")
        if decide3 == "scream":
            print "You hear some shuffling to your left."
            print "The wall above you opens."
            print """A group of police officers break you free and say
'You're safe now, there is no need to worry'
            """
        else:
            start()
    else:
        start()

def gum():
    print "You check your pockets and there is a piece of bubblegum."
    print "(ﾉﾟ0ﾟ)ﾉ Yum!"
    print "You chew the piece of gum."
    inventory.remove('gum')

# Getting an error and need to resolve: http://eli.thegreenplace.net/2011/05/15/understanding-unboundlocalerror-in-python
def escape():
    decide5 = raw_input("> ")
    if "run" in decide5:
        print "You start to run down to the bottom of the parking garage."
        end_of_line()
    elif "motorcycle" in decide5:
        print "You steal a motorcycle and start to drive down the parking garage."
        end_of_line()
    elif "car" in decide5:
        print "You steal a car and start to drive down the parking garage."
        end_of_line()
# test this scenario more, it seems to end the game
    elif "look" in decide5:
        print "You look around and see a bunch of cars and a few motorcycles."
        escape()
    elif "pocket":
        gum()
        print "Now what?"
        escape()
    else:
        print "Nothing happens"

def end_of_line():
    print "You've reached the bottom of the parking garage and you see a dark figure."
    print "You move closer and see its a strange looking man. He looks you in the eye and says 'How did you get out?'"
    decide6 = raw_input(">")
    if "motorcycle" in decide6:
        print "You speed up and try to aim your motorcycle at the standing figure."
        print "You miss and he grabs you and knocks you unconscious..."
        end1()
    elif "punch" in decide6:
        print "You try to punch him but he dodges and knocks you unconscious..."
        end1()
    elif "run" in decide6:
        print "You try to run past him but he grabs you and knocks you unconscious..."
        end1()
    elif "car" in decide6:
        print "You hit him with your car and he dies."
        end2()
    elif "shoot" in decide6:
        print "You shoot him and he dies."
    elif "pocket":
        gum()
        print "The man looks at you confused."
        print "Now what?"
        decide6 = raw_input(">")
    else:
        print "I don't understand that input."

def inventory():
    inventory = ['gum']
    print "Heres whats your inventory:"
    for item in inventory:
        print item

def end1():
    print "You see your arm go into a meat grinder and you get eatten by canabals."

def end2():
    print "You show up to work on time, no one notices anything."

print "You wake up in a small dark area."
start()
