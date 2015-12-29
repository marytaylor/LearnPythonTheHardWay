# ordinal == ordered
# cardinal == cards at random, 0

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print "Animal at 1 is %r" % animals[1]

print "The Third (3rd) animal is %r." % animals[2]

print "The first (1st) animal is %r." % animals[0]

print "The animal at 3 is %r." % animals[3]

print "The fifth (5th) animal is %r." % animals[4]

print "The animal at 2 is %r." % animals[2]

print "The sixth (6th) animal is %r." % animals[5]

print "The animal at 4 is %r." % animals[4]

print "These are the animals: "
print animals

# Drill 1: With what you know of the difference between these types of numbers,
#   can you explain why the year 2010 in "January 1, 2010," really is 2010 and
#   not 2009? (Hint: you can't pick years at random.)

# Based on the original exercise description it is because years are not random
#   so it cannot be cardinal; it is ordinal.

# Drill 2: Write some more lists and work out similar indexes until you can
#   translate them.

# Drill 3: Use Python to check your answers.

weapons = ['sword', 'dagger', 'pistol', 'shotgun', 'axe', 'grenades',
'plasma rifle', 'sniper rifle', 'mace']

print "If you really make me mad I will attack you with a %r!" % weapons[4]

print "If you catch me by surprise I may attack you with %r..." % weapons[8]

print "If I don't want you to remember anything, I'll use a %r." % weapons[7]

print """I will now give you a weapon at random.  Choose a number between 0
and 8."""

weapon_of_choice = input("> ")

print "Congrats! You have choosen a %r." % weapons[weapon_of_choice]
