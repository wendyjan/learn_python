

def squared(x):
    return x * 2


def cubed(x):
    return x ** 3


def new_py_pet():
    name = random.choose(["Spot", 
                          "Shadow", 
                          "Trixy", 
                          "Snuggles",  
                          "Fritz", 
                          "Cookie",
                          "Marshmallow"]
    animal_type = random.choose(["Dog",
                                 "cat",
                                 "penguin",
                                 "dolphin",
                                 "tiger",
                                 "chameleon",
                                 "horse"])
    fav_activity = random.choose(["snuggling",
                         "playing fetch",
                         "going for walks", 
                         "sleeping",
                         "eating",
                         "watching my human on the computer"
                         "learning tricks'])
    hungry = random.choose([True, False])
    sleepy = random.choose([True, False])
    return {'name': name, 
            'type': animal_type, 
            'favorite activity': fav_activity, 
            'hungry': hungry,
            'sleepy': sleepy,
            'age': age}

if __name__ == "__main__":
    print squared(5)
    print cubed(5
    print "My new PyPet:", new_py_pet
