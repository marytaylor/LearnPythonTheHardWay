ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# To python: split(ten_things, ' ') is assigned to stuff
# Call split argument on ten_things using ' '
stuff = ten_things.split(' ')
# Call split using ' ' on ten_things and then assign to stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
  # To python: pop(more_stuff) is assigned to next_one
  # Call pop with arugment of more_stuff and assigned to next_one
  next_one = more_stuff.pop()
  # Call pop on more_stuff
  print "Adding: ", next_one
  # To python: append(stuff, next_one)
  # Call append with argument of stuff using next_one
  stuff.append(next_one)
  # Call append on stuff using next_one
  print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
# To python: pop(stuff)
# Call pop with argument of stuff
print stuff.pop()
# Call pop on stuff

# To python: join(' ', stuff)
# Call join on ' ' using stuff
print ' '.join(stuff) # what? cool!
# Call join with argument of ' ' on stuff

# To python: join('#', stuff[3:5])
# Call join on '#' using stuff going through the 3rd 4th item
print '#'.join(stuff[3:5]) # super stellar!
# Call join with argument of '#' using the 3rd and 4th item in stuff



#1. Take each function that is called, and go through the steps for function
#   calls to translate them to what Python does. For example, more_stuff.pop()
#   is pop(more_stuff). - Completed above

#2. Translate these two ways to view the function calls in English. For example,
#    more_stuff.pop() reads as, "Call pop on more_stuff." Meanwhile,
#   pop(more_stuff) means, "Call pop with argument more_stuff." Understand how
#   they are really the same thing. - Completed above

#3. Go read about "object-oriented programming" online. Confused? I was too. Do
#   not worry. You will learn enough to be dangerous, and you can slowly learn
#   more later.
#   Liked this article: http://goo.gl/tdX0hT

#4. Read up on what a "class" is in Python. Do not read about how other languages
#    use the word "class." That will only mess you up.
#   Liked the docs: https://docs.python.org/2/tutorial/classes.html

#5. Do not worry If you do not have any idea what I'm talking about. Programmers
#   like to feel smart so they invented object-oriented programming, named it
#   OOP, and then used it way too much. If you think that's hard, you should try
#   to use "functional programming."
#   Liked this article: https://goo.gl/SAv0Kn

# Drill 6 in separate file ex38_Drill6.py
