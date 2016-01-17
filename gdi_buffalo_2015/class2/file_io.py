
import os


if __name__ == "__main__":
    
    # Read in a file.
    with open("input.txt", 'r') as f:
        text = f.readlines()
    print text

    # Write that to a new file, with a change!
    for i, line in enumerate(text):
        text[i] = line.upper()
    with open("output.txt", 'w') as f:
        for line in text:
            f.write(line)
    print 'All done!'

# which functions or methods are coming from os? Would assigning f = open ... be the same as the with-as? is there another purpose for the with- as?
# It took me awhile (in the past) to figure out that when you do things like this, your file, the new file and the program file all need to be in the same directory.
