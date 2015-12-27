# Write it to use for-loops and range. Do you need the incrementor in the middle
#   anymore? What happens if you do not get rid of it?

# The incrementor is no longer necessary and I cannot include my own incrementor
#   because range automatically goes 1 by 1; I think? I could not find another
#   way to increment with range.

print "What number would you like to end at?"

count = input("End at: ")

i = 0
numbers = []

for i in range(count):
    print "At the top i is %d" % i
    numbers.append(i)

    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num
