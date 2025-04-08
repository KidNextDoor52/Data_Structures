

class Users:
    """
    We are building a user class to store user attribute
    add_profile func: will add profiles to list user_profiles
    args:
        id - the unique id/key
        name - the users name
        age - users age
        permissions - user access based off ag

    """
    age = 0
    user_profiles = []
    def __init__(self, id, name, age, perms):
        self.id = id
        self.name = name
        self.age = age
        self.perms = perms

        n = Users(id=1, name="Robert", age=28, perms="Admin")
        if self.age < 1:
            print("Newborn")
        elif self.age <= 4:
            print("Toddler")
        #these will play a part in the list manipulation
        #elif age <= 12:
        #    print("Kid")
        #elif (age >= 13) and (age <= 19):
            print("Teen")
        else:
            print("Adult")

