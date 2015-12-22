# This defines the function named cheese_and_crackers using 2 named arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# First method in the function
    print "You have %d cheeses!" % cheese_count
# Second method in the function
    print "You have %d boxes of crackers!" % boxes_of_crackers
# Third method in the function
    print "Man that's enough for a party!"
# Fourth method in the function
    print "Get a blanket.\n"
# Function methods end here.

# Print text and our function created earlier with 2 values for arguments.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Print text
print "OR, we can use variables from our script:"
# Declare new variable
amount_of_cheese = 10
# Declare another new variable
amount_of_crackers = 50

# Call our function and give it the newly created variables.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print text and use function with math in arguments.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Print text and use function with math, variables and arguments.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Drill 1: type comment above each line explaining what it does.
# Drill 2: Read each line backward saying all the important characters.
# Drill 3: in new file.
