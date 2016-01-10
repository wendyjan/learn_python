
sum = sum + 1 
sum += 1

40/3

sum(L)
min(L)
max(L)

round(x,n)

abs()

math.sqrt()

math.sin()

random.random()

random.randint()

a = raw_input(“What is the value of a? “)

5 == 6
5==5
5 == ‘5’
6 <= 7
5!=5

5 != 1 or 5 == 1
4 < 5 and 1 < 4
1 < 4 < 5
a = 4
1 < a < 5
1 + 9 == 10 and 90 / 2 == 40      
not 5 == 1

“Munch”
‘Munch’		
“Wake up, kids!\n It\’s time for school.”



Escape sequences for special characters
\n
newline (a whitespace character)
\t
 tab (a whitespace character)
\’ or \”
quotes will be within string, or use raw string, rstring
\\
backslash will be within string, or use raw string by preceding the string with r
r
keeps backslashes as back slashes when it precedes a string


Try

print (r”C:\py\code”)

Make Python print the following conversation, using one print statement.
“That’s my boy,” said mom.
“The apple don’t fall too far from the tree,” said dad.


Common String Operations for a string S

len(S)
length of string
S * 3
repeat
S + “another string”
concatenate
S[i]
Uses index to select one character
S[i:j]
Slices a group of characters
S.find(‘c’)
Finds index (position) of given character
S.rstrip(), S.lstrip(), S.strip()
remove whitespace characters from right, left, or both sides
S.replace(‘cc’, ‘pa’)
replaces first string with second
S.split(‘,’)
split on delimiter, in this case a comma
S.lower(), S.upper()
change case
S.endswith(‘es’)
returns True or False depending if the string ends with es


Try 

S = “Happy Halloween, Best Witches!”
len(S)
S * 2
S + “Boo”
S
S[5]
S[4]
S[5:10]
S.find(’Witch’)
S.find(“a”)
S.replace(‘!’, ‘?’)
S.split(‘ ‘)
S.split(‘,’)
S.lower()
S


More on Indexing and Slicing 

An index is the position of a number when counting positions starts with 0. The first character in the string has index 0. 

A slice from i to j denoted [i:j] starts at i and ends before j.

[i:] fetches characters from i to the end of the string. [:j] fetches characters from the beginning.

A negative index starts at the right end with -1.

A step, k, can be used [i:j:k] in a slice. k can be positive or negative.

Picture it like this:

0         	1	2	3	4	5	6	7	8	9	10	
g
l
u
t
e
n


f
r
e
e
									-2	-1

Try
my_string = “gluten free”
my_string[0]
my_string[3:9]
my_string[:]
“gluten free”[3]
my_string[0:9]
my_string[:7]
my_string[2:]
my_string[-1:-5]
my_string[-5:-1]
my_string[0:11:3]
my_string[::-1]
my_string[0:2] + my_string[-2:]

Slice my_string to get the following outputs:
“free”
“u”
“tnf”

String formatting

