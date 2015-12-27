# Drill 3: Use this function to rewrite the script to try different numbers.
# Drill 4: Rewrite the script again to use this function to see what effect that
#    has.


print "What number would you like to end at?"

count = input("End at: ")

print "What value do you want to increment by?"

increment = input("Increments of: ")

i = 0
numbers = []

while i < count:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + increment
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num
