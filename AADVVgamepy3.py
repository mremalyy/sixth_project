import time
import random


Attackers = ["The wicked fairie", "The grogon",
                                  "the Dragon", "the Monsters", "snake"]
lists = random.choice(Attackers)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(ANS, one, two):
    while True:
        response = input(ANS).lower()
        if one in response:
            break
        elif two in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro():
    print_pause("You are too late for your business in the company")
    print_pause("You want to get to your company quickly")
    print_pause("while you were walking in a dark street,"
                "You found two different ways")


def reaction():
    response = valid_input("so where you prefer to go "
                           "way1 or way2 ? \n ",
                           "way1", "way2")
    if "way1" == response:
        print_pause("Excellent.You entered the right way.")
        print_pause("You arrived to your company as fast as possible")
        play_again()
    elif "way2" == response:
        print_pause("Wrong choice")
        print_pause(f"and the {lists} attacks you! \n")
        play_again()
    else:
        print_pause("Sorry, I don't understand")
        reaction()


def play_again():
    response = valid_input("Would you like to play again ? "
                           "Please enter 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" == response:
        print_pause("Wish you the best of luck")
    elif "yes" == response:
        print_pause("Very good, I'm ready to mess with you ")
        intro()
        reaction()
    else:
        print_pause("Sorry, I don't understand")
        return play_again()


def play_game():
    intro()
    reaction()
    play_again()


play_game()
