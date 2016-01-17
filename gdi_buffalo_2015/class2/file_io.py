
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

