hungry = raw_input(“Are you hungry? Type Y or N ”)
food = 0
if hungry == “Y”:
	print “Here is a treat for you.”
	food = food + 1
else:
	print “okay”

pigs = “fly”
if pigs = “fly”:
print “This prints.”
else:
print “This does not print.”	

import random
x = random.randint(-10,10)
if x < 0:
	sign = “negative”
elif x ==0:
	sign = “none”
else:
	sign = “positive”
print sign, x

sign = “positive” if x > 0 else “negative”

grade = raw_input(“Enter a whole number grade between 0 and 100 “)
if grade > 90:
	print “A”
elif grade < 90 and grade > 80:
	print “B”

grade = raw_input(“Enter a whole number grade between 0 and 100 “)
if grade > 90:
	print “A”
elif grade > 80:
	print “B”
elif grade > 70:
	print "C"
elif grade > 60
	print "D"
else:
	print "F"

x = 1
y = 2
if x == 1 and y > 1:
	if y == 1:
		print “tomato”
	print “potato”
print “cabbage”

x = ‘sand’
if ‘sand’ in ‘sandwiches’:
	print x*3
	x += ‘wich’
	if x.endswith(‘wich’):
		x *=2
		print x

x = [1,3,5,7,11]
if x[0:2] != [1,3]:
	print ‘nope’
	if x[4] == 11:
		print ‘yup’
else:
	print ‘yup yup’
