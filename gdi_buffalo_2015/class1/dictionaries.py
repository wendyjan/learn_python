"""
filename: dictionaries.py
author: wendyjan

This file shows dictionaries in Python.
"""

if __name__ == "__main__":
    # Make a new dictionary, using { instead of [.
    # Each pair of (key, value) items is connected with a colon.
    my_dict = { "Wendy": "Jansson", "Joe": "Jones", "Clara": "Rodriquez"}
    print my_dict
    print my_dict["Wendy"]
    
    # Add a new person to our dictionary.
    my_dict["Carey"] = "Forester"
    print my_dict["Carey"]
    print my_dict
    
    # Can we store two different Claras?
    my_dict["Clara"] = "Wu"
    print my_dict["Clara"]

    #print my_dict["Anne"] # Comment this line out unless you want an error!

    # Store a PyPet in a dictionary.
    monty = {"age": 3, "name": "Monty", "type": "doberman"}
    for k in monty.keys():
        print k, ":", monty[k]
    
    # Store employees and update the dictionary when they come and go.
    emps = {1: "Rich Simons", 2: "Natalia Burges", 3: "Adrianne Velasquez", 4: "Ying Su"}
    print emps
    print "There are", len(emps), "total at the start."
    emps[5] = "Thomas Hah"
    emps.remove(3)
    print "After some changes, the employee list is:", emps.values()
