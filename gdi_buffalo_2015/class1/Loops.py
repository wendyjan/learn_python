dogs = [‘Rover’, ‘Max’, ‘Holly’]
for dog in dogs:
	dog = dog + ‘\’s’
	print dog
	
for letter in “word”:
	print letter + “uba”

ages_later = []
years = 10
ages = [12, 15, 17]
for age in ages:
	age +=years
	ages_later.append(age)
print ages_later

range(5)

for x in range(5):
	print x**2

ages_later = []
years = 10
for age in range(12,18):
	age +=years
	ages_later.append(age)
print ages_later

dogs = [‘Rover’, ‘Holly’]
for i in range(len(dogs)):
	dogs[i] = dogs[i] + ‘\’s’
print dogs

cards = [‘ace’, 2,3,4,’queen’]
for i in range(len(cards)):
	cards = cards[i:] + cards[:i]
	print cards

multiples_of_two_and_three = []
for x in range(100):
	if x%2 == 0 and x%3==0:
		multiples_of_two_and_three.append(x)
print multiples_of_two_and_three

for i, day in enumerate([Mon, Tue, Wed, Thurs, Fri]):
	print i, day

food = 0
while food < 5:
hungry = raw_input(“Are you hungry? Type Y or N ”)
if hungry == “Y”:
		print “Here is a treat for you.”
		food += 1
print “I feel full”

food = 0
while food < 5:
	hungry = raw_input('Are you hungry? Type Y or N ')
	if hungry == 'Y':
		print 'Here is a treat for you.'
		food += 1
	else:
		break
else:
	print "I sure was hungry!"
print 'Now what?'

dogs = [‘Holly’, ‘Max’, ‘Sadie’, ‘Joey’]
while dogs:					#unempty lists have the boolean value of True
	print dogs.pop(0) + “ barks.”		# pop gets an item AND removes it from the list
	print dogs

dogs = ['Holly','Max','Sadie','Joey']
i = 0
while len(dogs) > 1:
	if dogs[i] == 'Sadie':
		i=1
		continue
	print dogs.pop(i) + " barks"
	print dogs

x = 10
while x:			#remember x has the boolean value of True
	x = x-1
	if x % 2 != 0:
		continue
	print x

x = 11
while x > 10:
	print “uh oh”

while True:
	print “uh oh”

dogs = [‘Rover’, ‘Max’, ‘Holly’]
toys = [‘bone’, ‘squirrel’]
for dog in dogs:
	for toy in toys:
		print ‘That is ‘ + dog + ‘\’s ’ + toy + ‘.’
	
	print “That is %s\’s %s.” % (dog,toy)

items = [“aaa”, 111, (4,5), 2.01]
tests = [(4,5), 3.14]
for thing in tests:
	for item in items:
		if item == thing:
			print thing + “was found”
		else:
			print thing + “was not found”

	

