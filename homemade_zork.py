#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

# Getting an error and need to resolve: http://eli.thegreenplace.net/2011/05/15/understanding-unboundlocalerror-in-python
def escape():
    if "run" in decide5:
        print "You start to run down to the bottom of the parking garage."
    elif "motorcycle" in decide5:
        print "You steal a motorcycle and start to drive down the parking garage."
    elif "car" in decide5:
        print "You steal a car and start to drive down the parking garage."
    elif "look" in decide5:
        print "You look around and see a bunch of cars and a few motorcycles."
    elif "pocket":
        gum()
        decide5 = raw_input("> ")
    else:
        print "Nothing happens"

def start():
    print "Your arms are tied behind you."
    print "What do you do now?"

    decide1 = raw_input("> ")

    if decide1 == "scream":
        scream()

    elif "feel" in decide1:
        print "You feel something that feels like a hook on the wall behind your back."
        decide4 = raw_input("> ")
        if "pull" or "tag" or "grab" or "grasp" in decide4:
            print "The wall above you opens and you realize you were in the trunk of a car."
            print "As you look around you see several vehicles; you must be in a parking garage."
            decide5 = raw_input("> ")
            escape()
        elif "pocket" in decide4:
            gum()
            decide5 = raw_input("> ")
        else:
            nothing()
            start()
    elif "pocket" in decide1:
        gum()
    else:
        print "Nothing happens"
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



print "You wake up in a small dark area."
start()
