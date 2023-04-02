
import random

name = input("Please enter your name:")
num_of_games = input("How many games would you like to play?")
print()

round = 1
play_score = 0
comp_score = 0

# This is the function for the player's selection.


def players_choice():
    your_move = input("Please make your move, R, P, S :")
    if your_move == ("R"):
        print(name, ", You Choose Rock!")
        return 0
    elif your_move == ("P"):
        print(name, ", You Choose Paper!")
        return 1
    elif your_move == ("S"):
        print(name, ", You Choose Scissors!")
        return 2
    else:
        print("Sorry, That is an invalid choice, Please select R, P or S. in CPAS with no spaces!")
        return players_choice()

# This is the function for the computer's selection.


def comp_choice():
    comp_range = ("0", "1", "2")
    comp_weppon = random.choice(comp_range)
    if comp_weppon == ("0"):
        print("Computer picks Rock!")
        return 0
    elif comp_weppon == ("1"):
        print("Computer picks Paper!")
        return 1
    elif comp_weppon == ("2"):
        print("Computer picks Scissors!")
        return 2

# This is the scoreing function.


def score():
    #if int(comp_choice()) == int(players_choice()):
    if players_weppon == comp_weppon:
        print("Draw!")
    elif (players_weppon == "0" and comp_weppon == "2") or (players_weppon == "1" and comp_weppon == "0") or (players_weppon == "2" and comp_weppon == "1"):
        global play_score
        play_score += 1
        print("You Win!")
    elif (players_weppon == "0" and comp_weppon == "1") or (players_weppon == "1" and comp_weppon == "2") or (players_weppon == "2" and comp_weppon == "0"):
        global comp_score
        comp_score += 1
        print("You Lose!")
    else:
        print("Void")

# This is a loop to tally the score.


while round <= int(num_of_games):
    print("*"*40)
    print("*             Round #", round, "               *")
    print("*"*40)
    players_weppon = str(players_choice())
    comp_weppon = str(comp_choice())
    score()
    print()
    print("*"*40)
    print("*  Overall Score:", name, play_score, "Computer", comp_score, "  *")
    print("*"*40)
    print()
    round += 1

print("------Thank you for playing", name,"------")
