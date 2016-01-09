def credits():
	print “This example was borrowed from \’Learning Python\’ by Mark Lutz.”

credits()
	
def tip(percentage, total):
	return round(percentage * total/100,2)

tip(15,24.50)

print tip(15,24.50)

bill = raw_ input(“What did your bill come to?”)
p = raw_input(“What percentage would you like to use for the tip?”)
print ‘tip is’ tip(float(p), float(bill)) #show float conversion outside

total_tips = 0
for transaction in range(8):
	# random amount from bills
	total = float(randrange(2000,4000)/100)
	tip_percent = float(randrange(15,20))
	total_tips += tip(tip_percent, total)
print total_tips

def salutation(person, gender):
	if gender = “female” or gender == “f”:
		print “Ms. “ + person
	else:
		print “Mr. “ + person

team = {‘Izydorczak’:”female”, ‘Jansson’:”female”, ‘Ryan’’:”male”]
for member in team:
	print “Hi “
	salutation(member, team[member])

def express_happy():
	say_options =[“I love you!”, “Hip hip hurray!”, “Purr, Purr, I’m happy!”]
	print random.choice(say_options)

import random
hungry = random.randint(0,10)
if hungry < 5:
	print “Hungry”
else:
	express_happy()

import random
def express_happy(owner):
	say_options = [“I love you “ + owner + “!”, “Hip hip hurray!”]
	print random.choice(say_options)

drawSquare()
drawSquare(x,y)
scissors(newspaper)	#not real python
longReacher(object)	#not real python
quadraticFormula(a,b,c)
fahrenheitConverter(degrees_celsius)
