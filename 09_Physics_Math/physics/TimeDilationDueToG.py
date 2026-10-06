import math

CONDITION = True
C = 299792458
G = 6.674**-11
while CONDITION is True:
    try:
        T = int(input("Enter time measured by an observer: "))
        M = int(input("Enter the mass of object/planet creating gravity: "))
        R = int(input("Enter the radius distance from the center of the mass to observer: "))
    except ValueError:
        print("You are supposed to enter a number")

    
    else:
        t = T*math.sqrt((1 - (G*M) / (R*(C)**2)))
        print(f"\n Result: {t} sec")
        print("\n Thank You!!")
        CONDITION = False