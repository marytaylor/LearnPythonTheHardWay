from sys import argv

script, user_name, age = argv
prompt = '--> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "You're %s years old so," % age
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alight, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# Drill 1: Find out what Zork and Adventure were.  Try to find a copy and play it.
# This should be interesting...
# Just lost 30 minutes on Zork haha.
# Tried Adventure but Zork was way better.
