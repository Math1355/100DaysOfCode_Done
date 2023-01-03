
def barbecue_grill():

    skewers = ["--oooo-ooo--",
           "--xxxxxxxx--",
           "--o--o-",
           "-o-----o---x--",
           "--o---x-----",
           "--xxxx-----",
           "--o---xo-----",
           "--o---o-----"]

    vegetarian = 0
    no_vegetarian = 0

    for spit in skewers:
        print(spit)
        with_meat = spit.find("x")
        if (with_meat >= 0):
            no_vegetarian += 1
        else:
            vegetarian += 1
    
    

    return f'We have {vegetarian} vegetarian skewers, {no_vegetarian} non-vegetarian skewers!'