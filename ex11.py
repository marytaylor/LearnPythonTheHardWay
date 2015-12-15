print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
 age, height, weight)

# Drill #1 Go online and find out what Python's raw_input does.
# This function reads a line from input, converts it to a string (stripping a trailing newline), and returns that.

# Drill #2 Can you find other ways to use it? Try some of the samples you find.

x = raw_input()
print x

y = raw_input('-->')
print y

name = raw_input('Enter your name : ')
print ("Hi %s, Let us be friends!" % name);

# Drill #3 Write another "form" like this to ask some other questions.

print "This is a user survey.  Please answer with a value of 1-5."

print "Question 1: Is the website easy to navigate?"
question1 = raw_input()

print "Question 2: Is the information easy to find?"
question2 = raw_input()

print "Question 3: Would you recommend this website to a friend?"
question3 = raw_input()

print "Thank you for taking the survey!"

# Drill #4 Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence.
# See how the single-quote needs to be escaped because otherwise it would end the string?

#Interesting fact, raw_input() is better to use because input() has security issues.  Look into this more
