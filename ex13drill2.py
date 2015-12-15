# Drill: Combine raw_input with argv to make a script that gets more input
#    from a user.

from sys import argv

script, x, y, z = argv

print "What is x?"
x = raw_input()
print "What is y?"
y = raw_input()
print "What is z?"
z = raw_input()

print "You choose x as:", x
print "You choose y as:", y
print "You choose z as:", z
