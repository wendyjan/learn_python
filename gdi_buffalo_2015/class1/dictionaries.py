"""
filename: dictionaries.py
author: wendyjan

This file shows dictionaries in Python.
"""

if __name__ == "__main__":
    my_dict = { "Wendy": "Jansson", "Joe": "Jones", "Clara": "Rodriquez"}
    print my_dict

    print my_dict["Joe"]
    my_dict["Dave"] = "Wu"
    print my_dict["Dave"]

    my_dict["Joe"] = "Forester"
    print my_dict["Joe"]
    print my_dict

    #print my_dict["Anne"] # Comment this line out unless you want an error!

    # Store a PyPet in a dictionary.
    monty = {"age": 3, "name": "Monty", "type": "doberman"}
    for k in monty.keys():
        print k, ":", monty[k]
