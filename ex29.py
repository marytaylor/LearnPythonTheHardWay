people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

print "People: %d" % people
print "Dogs: %d" % dogs
print "Cats: %d" % cats

if people >= dogs and dogs < cats:
    print "The world is rolling along smoothly."

# Drill 1: What do you think the if does to the code under it?
# It checks if it is true so that it can run it.

# Drill 2: Why does the code under the if need to be indented four spaces?
# To let the if statement know to run those lines for its function.  Kind of
#   like defining functions.

# Drill 3: What happens if it isn't indented?
# I guessed that it would not know that line was included with the if statement.
#   I tested the theory and received an error messages when I tried to run the
#   script. "IndentationError: expected an indented block"

# Drill 4: Can you put other boolean expressions from Exercise 27 in the
#   if-statement? Try it.
# Yes, also tested it and it worked.

# Drill 5: What happens if you change the initial values for people, cats and
#   dogs?
# The outputs would change depending on the values input. 
