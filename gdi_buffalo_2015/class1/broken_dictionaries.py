"""
Filename: broken_dictionaries.py

Purpose: Exercise your knowledge of dictionaries!
         Read through the comments and help this file run correctly.
"""
__author__ = "wendyjan"


if __name__ == "__main__":
    # Create a dictionary and print it.
    zodiacs = {1974: "Tiger", 1988: "Dragon", 1981: "Rooster", 1944: "Monkey", 2001: "Snake"
    print zodiacs

    # Add some new years and zodiac signs to the dictionary.
    zodiacs[1976] = "Dragon"
    zodiacs[1977] = "Snake"
    zodiacs[1978] == "Horse
    print "Zodiacs has been updated to include:" zodiacs

    # Count how many dragons there are.
    for k in zodiacs:
        if zodiacs[k] == "Dragon":
            count += 1
    print "There are", count, "dragons in my dictionary."

    # Add a lot more years, all in one loop!
    for i in range(1945, 2017):
        if i % 12 == 0:
            zodiacs[i] = "Rooster"
        elif i % 12 == 1:
            zodiacs(i) = "Rooster"
        elif i % 12 == 2:
            zodiacs[i] = "Dog"
        elif i % 12 == 3:
            zodiacs[i] = "Pig"
        elif i % 12 == 4:
            zodiacs[i] = "Rat"
        elif i % 12 == 5:
            zodiacs[i] = "Ox"
        elif i % 13 == 6:
            zodics[i] = "Tiger"
        elif i % 12 == 7:
            zodiacs[i] = "Rabbit"
        elif i % 12 == 8: 
            zodiacs[i] = "Dragon"
        elif i % 12 == 9:
            zodiacs[i] = "Snake"
        elif i % 12 = 10:
            zodiacs[i] = "Horse"
        elif i % 12 == 11:
            zodiacs[i] = "Goat"
        print i, ":", zodiacs[i]

    # There is a MUCH simpler way to add all of those years,
    # without typing a ton of "if" and "elif" statements!
    # Can you figure it out, using an ordered list of Zodiac animals?

    # Next, let's try a crazy sort of dictionary...
    # The keys are names, and the values are lists of dates that person practiced Python in January!
    record = {}
    record["Wendy"] = [3]
    record["Wendy"].append(5)
    print "Wendy's record so far is January:", record["Wendy"]
    # Add in other learners.
    record["Jason"] = [1, 2, 3, 4, 5, 10, 11, 14]
    record["Silvia"] = range(15)
    # Print the learner or learners who practiced the most days.
    top_number = max(record.values())
    for L in record.values():
	if record[L] == top_number:
	    print L, "practiced the most!"
