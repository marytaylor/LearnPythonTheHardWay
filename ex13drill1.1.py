#Drill 2.1 (drill 1 was in the first file), write a scrip with fewer arguemnts
from sys import argv

script, x, y = argv

# For some reason, if I did not add script then my print function for y did not run.
# I will need to look into that.
print script
print x
print "this is a test", y
