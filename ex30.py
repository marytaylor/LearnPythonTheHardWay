people = 30
cars = 15
trucks = 15

# when cars are greater than people print this line.
if cars > people:
    print "We should take the cars."
# when cars are less than people print this line.
elif cars < people:
    print "We should not take the cars."
# when cars and people are equal print this line.
else:
    print "We can't decide."

# when trucks are greater than cars print this line.
if trucks > cars:
    print "That's too many trucks."
# when trucks are less than cars print this line.
elif trucks < cars:
    print "Maybe we could take the trucks."
# when trucks and cars are equal print this line.
else:
    print "We still can't decide."

# when people are greater than trucks print this line.
if people > trucks:
    print "Alright, let's just take the trucks."
# when peoplare are less than trucks or equal print this line.
else:
    print "Fine, let's stay home then."

if people == trucks or trucks == cars:
    print "Thats an interesting similarity."
