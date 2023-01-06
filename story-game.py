## two persons talking tour plan ##
print("Hi Buddy what's your name")
n1 = input()

print("Hello "+n1+" Please tell your good friend name")
n2 = input()

print("you two talking about going on a trip yesterday evening")
n3 =input()

if n3 == 'yes':
    print("Ok " + n1 + " which place select on your trip")
    place1 = input()

    print("Ok " + n1 + " have you already been to " + place1)
    n4 = input()

    if n4 == 'yes':
        print("Hey " + n1 + " how many times you visiting in " + place1)
        t1 = input()
        print("Ho supper " + n1)

        print("Ok " + n1 + "I am joining your trip")
        t4 = input()
        if t4 == 'ok':
            print("Ok thank you " + n1)
        elif t4 == 'no':
            print("ok no problem " + n1 + "enjoy your trip")

    elif n4 == 'no':
        print("Ok "+n1+" your friend " + n2 + " already been to " + place1)
        t2 = input()

        if t2 =='yes':
            print("Ok "+n1+" your friend " + n2 + " how many times you visiting in " + place1)
            t3 = input()
            print("Ho supper")

            print("Ok "+n1+ "I am joining your trip")
            t5 = input()
            if t5 == 'ok':
                print("Ok thank you "+n1)
            elif t5=='no':
                print("ok no problem "+n1+ "enjoy your trip")

        elif t2 =='no':
            print(" Ho nice both of you are going for the first time " + place1)

else:
    print("ok thank you "+n1)
