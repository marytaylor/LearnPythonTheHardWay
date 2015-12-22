# Drill 3: Write at least one more function of your own design, and run it 10
# different ways.
def decorate_tree(ornaments, candy_canes):
    print "You have %s ornaments!" % ornaments
    print "You have %s candy canes!" % candy_canes
    print ("Thats an awesome christmas tree.")

# 1st way:
print "How many ornaments do you have?"
your_ornaments = raw_input()
print "How many candy canes do you have?"
your_candy_canes = raw_input()
decorate_tree(your_ornaments, your_candy_canes)

# 2nd way:
print "\n"
print "Try it with hardcoded values:"
decorate_tree(2,5)

# 3rd way:
print "\n"
print "Try it with math:"
decorate_tree(34+5, 0+6)

# 4th way:
print "\n"
print "Try it with variables:"
new_ornaments = 5
new_candy_canes = 3
decorate_tree(new_ornaments, new_candy_canes)

# 5th way:
print "\n"
print "Try with variables and math:"
decorate_tree(new_ornaments + 6, new_candy_canes + 4)

# 6th way:
print "\n"
print "How many candy canes and ornaments do you have?"
ornaments = raw_input('Ornaments:')
candy_canes = raw_input('Candy Canes:')
decorate_tree(ornaments, candy_canes)

# 7th way:
print "\n"
print "With raw input and math:"
print "How many ornaments do you want to add?"
# raw_input did not work here because it had to be a integer
some_ornaments = input()
# raw_input did not work here because it had to be a integer
print "How many candy_canes do you want to add?"
some_candy_canes = input()
print "I'm going to add 5 more ornaments and 5 more candy canes."
decorate_tree(some_ornaments + 5, some_candy_canes + 5)

# 8th way:
x = 100
y = 1000
decorate_tree(some_ornaments + x, some_candy_canes + y)

# 9th way:
# I'm running out of ideas so I need to go back further in lessons.
from sys import argv
script, filename1, filename2 = argv

newer_ornaments = open(filename1).read()
newer_candy_canes = open(filename2).read()
# close is not necessary here
decorate_tree(newer_ornaments, newer_candy_canes)

#10th way:
ornaments = len(newer_ornaments)
candy_canes = len(newer_candy_canes)
decorate_tree(ornaments, candy_canes)
