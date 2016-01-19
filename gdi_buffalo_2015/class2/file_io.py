"""
filename: file_io.py
author: wendyjan

This file shows a simple file input/output example.
"""

if __name__ == "__main__":
    
    # Read in a file.
    # Note that your input file and the program file need to be in the same directory!
    with open("input.txt", 'r') as f:
        text = f.readlines()
    print text

    # Write that to a new file, with a change!
    # The output file will be written to the same directory.
    for i, line in enumerate(text):
        text[i] = line.upper()
    with open("output.txt", 'w') as f:
        # Use the 'with' keyword to protect a resource.
        # Even if an error occurs within the 'with' block,
        # this way the file will still be closed properly!
        for line in text:
            f.write(line)
    print 'All done!'
