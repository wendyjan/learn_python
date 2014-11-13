"""
Sample code for Intro to Python, Class 2.

Version 3, the last version we looked at together.
"""

class Store:

    def __init__(self, newName):
        # assert(isinstance(newName, str))

        assert(type(newName) == str)
        self.DEBUG = True
        self.name = newName
        if self.DEBUG:
            print("Store name is: " +  self.name)
        self.items = []

    def addItem(self, item, cost):
        assert(type(cost) == int)
        newPair = [item, cost]
        self.items.append(newPair)
        if self.DEBUG:
            print ("Item added: " + str(item) + ", cost: " + str(cost))

    def sellItem(self, sellMe):
        for i in range(len(self.items)):
            if self.items[i][0] == sellMe:
                itemToRemove = self.items.pop(i)
                break
                #return itemToRemove # RETURN SOMETHING HERE!

        print ("Item not found: " + str(sellMe))

    def getAllItems(self):

        stringToReturn = "Inventory of " + self.name + ": " + "\n"

        for item in self.items:
            thing = item[0]
            if self.DEBUG:
                print("Store thing: " + thing)
            cost = item[1]
            if self.DEBUG:
                print("Thing cost: " +  str(cost))
            stringToReturn += ("Item: " + str(thing) + ", cost: " + str(cost))
            stringToReturn += "\n"

        return stringToReturn

if __name__ == "__main__":

    myStore = Store("711")
    myStore.addItem("Ice cream", 5)
    myStore.sellItem("jelly")











    
