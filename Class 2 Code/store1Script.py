from store1 import Store

if __name__ == "__main__":

    myStore = Store("Wegmans")

    print (myStore.name)

    myStore.addItem("Ice cream", 5.95)

    print (myStore.getAllItems())

    

    
