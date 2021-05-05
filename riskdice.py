import random


def roll():  # Simple roll of a singular die
    return random.randint(1, 6)


def one_v_one(stat = None):  # 1 red vs 1 blue dice roll - stat is for calculating probabilities
    r1 = roll()
    b1 = roll()

    print("Red rolls a %i" % r1)
    print("Blue rolls a %i" % b1)
    if b1 >= r1:
        print("Blue wins!\n\n")
        if stat == "stat":
            return "Blue"
    else:
        print("Red wins!\n\n")
        if stat == "stat":
            return "Red"
    input("Press enter to continue...\n\n")
    menu()


def two_v_one(stat = None):  # 2 red vs 1 blue dice roll
    red = []
    r1 = roll()
    r2 = roll()
    b1 = roll()
    print("Red rolls a %i" % r1)
    print("Red rolls a %i" % r2)
    print("Blue rolls a %i" % b1)

    red.append(r1)
    red.append(r2)
    red.sort(reverse=True)

    if red[0] > b1:
        print("\nRed wins with a %i vs %i\n\n" % (red[0], b1))
        if stat == "stat":
            return "Red"
    else:
        print("\nBlue wins with %i vs %i\n\n" % (b1, red[0]))
        if stat == "stat":
            return "Blue"
    input("Press enter to continue...\n\n")
    menu()


def one_v_two():
    blue = []
    r1 = roll()
    b1 = roll()
    b2 = roll()
    print("Red rolls a %i" % r1)
    print("Blue rolls a %i" % b1)
    print("Blue rolls a %i" % b2)

    blue.append(b1)
    blue.append(b2)
    blue.sort(reverse=True)

    if r1 > blue[0]:
        print("\nRed wins with a %i vs %i" % (r1, blue[0]))
        print("Blue loses 1 unit\n\n")
    else:
        print("\nBlue wins with a %i vs %i" % (blue[0], r1))
        print("Red loses 1 unit\n\n")
    input("Press enter to continue...\n\n")
    menu()


def two_v_two():  # 2 red vs 2 blue dice roll
    red = []
    blue = []

    r1 = roll()
    r2 = roll()
    b1 = roll()
    b2 = roll()

    print("Red rolls a %i" % r1)
    print("Red rolls a %i" % r2)
    print("Blue rolls a %i" % b1)
    print("Blue rolls a %i" % b2)

    red.append(r1)
    red.append(r2)
    red.sort(reverse=True)
    blue.append(b1)
    blue.append(b2)
    blue.sort(reverse=True)

    bluecount = 0
    redcount = 0

    if red[0] > blue[0]:
        redcount += 1
        print("\nRed wins with a %i vs %i" % (red[0], blue[0]))
    else:
        bluecount += 1
        print("\nBlue wins with a %i vs %i" % (blue[0], red[0]))

    if red[1] > blue[1]:
        redcount += 1
        print("Red wins with a %i vs %i" % (red[1], blue[1]))
    else:
        bluecount += 1
        print("Blue wins with a %i vs %i" % (blue[1], red[1]))

    print("\nRed loses %i unit(s)" % bluecount)
    print("Blue loses %i unit(s)\n\n" % redcount)
    input("Press enter to continue...\n\n")
    menu()


def three_v_one():
    red = []

    r1 = roll()
    r2 = roll()
    r3 = roll()
    b1 = roll()

    print("Red rolls a %i" % r1)
    print("Red rolls a %i" % r2)
    print("Red rolls a %i" % r3)
    print("Blue rolls a %i" % b1)

    red.extend((r1, r2, r3))
    red.sort(reverse=True)

    if red[0] > b1:
        print("\nRed wins with a %i vs %i\n\n" % (red[0], b1))
    else:
        print("\nBlue wins with a %i vs %i\n\n" % (b1, red[0]))
    input("Press enter to continue...\n\n")
    menu()



def three_v_two():
    red = []
    blue = []

    r1 = roll()
    r2 = roll()
    r3 = roll()
    b1 = roll()
    b2 = roll()

    print("Red rolls a %i" % r1)
    print("Red rolls a %i" % r2)
    print("Red rolls a %i" % r3)
    print("Blue rolls a %i" % b1)
    print("Blue rolls a %i" % b2)

    red.extend((r1, r2, r3))
    red.sort(reverse=True)
    blue.extend((b1, b2))
    blue.sort(reverse=True)

    redcount = 0
    bluecount = 0

    if red[0] > blue[0]:
        redcount += 1
        print("\nRed wins with a %i vs %i" % (red[0], blue[0]))
    else:
        bluecount += 1
        print("\nBlue wins with a %i vs %i" % (blue[0], red[0]))

    if red[1] > blue[1]:
        redcount += 1
        print("Red wins with a %i vs %i" % (red[1], blue[1]))
    else:
        bluecount += 1
        print("Blue wins with a %i vs %i" % (blue[1], red[1]))

    print("\nRed loses %i unit(s)" % bluecount)
    print("Blue loses %i unit(s)\n\n" % redcount)
    input("Press enter to continue...\n\n")
    menu()

print()

def menu():
    print("1) 1 red vs 1 blue")
    print("2) 1 red vs 2 blue")
    print("3) 2 red vs 1 blue")
    print("4) 2 red vs 2 blue")
    print("5) 3 red vs 1 blue")
    print("6) 3 red vs 2 blue")
    print("\nChoose how many dice: ")
    x = int(input())
    if x == 1:
        one_v_one()
    elif x == int(2):
        one_v_two()
    elif x == int(3):
        two_v_one()
    elif x == int(4):
        two_v_two()
    elif x == int(5):
        three_v_one()
    elif x == int(6):
        three_v_two()
    else:
        print("Invalid selection\n\n")
        input("Press enter to continue...\n\n")
        menu()

menu()

#one_v_one()
#two_v_one()
#one_v_two()
#two_v_two()
#three_v_one()
#three_v_two()
