# Drill 1: Convert this while-loop to a function that you can call, and replace
#   6 in the test (i < 6) with a variable.
# Drill 2: Use this function to rewrite the script to try different numbers.
print "What number would you like to end at?"

count = input("End at: ")

i = 0
numbers = []

while i < count:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num
