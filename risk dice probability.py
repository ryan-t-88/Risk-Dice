import riskdice

# print("Test the probability of particular Risk dice roll combinations\n")
#
# def menu():
#     print("1 - one_v_one")
#     print("2 - one_v_two")
#     print("3 - two_v_one")
#     print("4 - two_v_two")
#     print("5 - three_v_one")
#     print("6 - three_v_two")
#
#     x = input("Which test would you like to run?")
#     y = input("How many times would you like to run the test?")
#
#     test(x,y)
#     menu()

# -------------------------------------------------------------------------

def test(roll, num):
    blue_tally = 0
    red_tally = 0
    for i in range(num):
        if roll == int(1):
            result = riskdice.two_v_one("stat")
            if result == "Red":
                red_tally += 1
            else:
                blue_tally += 1
    print("Blue wins: %i%%" % int(blue_tally/100))
    print("Red wins: %i%%" % int(red_tally/100))



test(1,10000)



