import art
from game_data import data
import random
import os



def create_account(exclude=None):
    """
    Selects and returns a random account from the data list.
    If an account is provided in `exclude`, the function ensures
    that the returned account is different from it.
    """
    choice = (random.choice(data))
    while choice == exclude:
        choice = random.choice(data)
    return choice

def format_data(account):
    """
    Formats an account dictionary into a readable string
    containing the name, description, and country.
    """
    return f'{account["name"]}, {account["description"]}, from {account["country"]}'

def is_win(guess , compare_a , compare_b):
    """
    Determines whether the user's guess is correct.

    Returns True if the guessed option ('a' or 'b') corresponds
    to the account with the higher follower count.
    """
    correct_answer = "a" if compare_a > compare_b else "b"
    return guess==correct_answer

def valid(guess):
    """
    Checks whether the user's input is a valid guess.

    A valid guess must be either 'a' or 'b'.
    """
    return guess in ("a", "b")

score = 0
compare_a = create_account()
while True:
    os.system("clear")
    compare_b = create_account(compare_a)
    print(art.logo)
    print(f"Compare A: {format_data(compare_a)}")
    print(art.vs)
    print(f"Compare B: {format_data(compare_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if valid(guess):
        if is_win(guess=guess , compare_a=int(compare_a["follower_count"]) , compare_b=int(compare_b["follower_count"])):
            score += 1
            print(f"You're right! Current score: {score}.")
            compare_a=compare_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    else:
        os.system("clear")
        print("Invalid input. Game over.")
        break