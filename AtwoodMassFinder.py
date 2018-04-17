done = False
m1 = None
mp = None
a = None


def calc_mass(m1, mp, a, g=9.82):
    m2 = ((m1 * (g - a)) / (a + g)) - ((mp * a) / (2 * (a + g)))
    return m2


while not done:
    m1 = float(input("What is the known mass?(kg): "))
    mp = float(input("What is the mass of the pully?(kg)"))
    a = float(input("What is the acceleration of the masses?(m/s^2): "))
    m2 = calc_mass(m1, mp, a)
    print("The unknown mass is:", m2, "kg")
    answer = input("Would you like to do another? (y/n): ")
    if answer.lower() == 'y':
        print("Again it is!")
        continue
    elif answer.lower() == 'n':
        print("Guess not...")
        done = True
    else:
        print("You entered something other than y or n so we are just going to quit anyway")
        done = True
