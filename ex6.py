# when **** is in a comment that means that it uses a string inside of a string

# This declares a variable that uses a string, with string formatting (integer decimal to be specific) inside of it.  The string formatting uses the value at the end.
x = "There are %d types of people." % 10
#This declares a variable that uses a string.
binary = "binary"
#This also declares a variable that uses a string.
do_not = "don't"
# **** This also declares a variable that uses string formatting (specifically a string formatter).
y = "Those who know %s and those who %s." % (binary, do_not)

#This prints the x variable
print x
#This prints the y variable
print y

# **** This declares a string wih a string formatter for variable x
print "I said: %r." % x
# **** this declares a string with a string formatter for variable y
print "I also said: '%s'." % y

#this declared the hilarious variable as false
hilarious = True
#this declares the joke_evaluation variable as a string with a string formatter for whatever value is given to it.
joke_evaluation = "Isn't that joke so funny?! %r"

# **** This prints a variable and uses a another variable
print joke_evaluation % hilarious

# This is giving a variable a string
w = "This is the left side of..."
#This is giving a variable a string
e = "a string with a right side."

#This will print two variables together.
print w + e
