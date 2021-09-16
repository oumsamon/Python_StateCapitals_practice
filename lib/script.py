from capitals import states

# print(states)

def welcome_msg():
    print("Welcome to match the State to the capitals game! \nType in the capital of the state that is being displays. \nThe result will be at the end of the game ")

# welcome_msg()

def capital_game():
    correct_score = 0
    incorrect_score = 0
    # cant use global vars in python to use inside a function.
    for i in range(0, len(states)):
        # print(i)
        player_answer = input(f'What is the Capital of {states[i]["name"]} ?')
        if player_answer.lower() == states[i]["capital"].lower():
            correct_score += 1
        else:
            incorrect_score += 1
    print(f'Thank you for playing! \nYour correct score: {correct_score} \nYour incorrect score: {incorrect_score} ')

capital_game()
print("Would you like to play again?  Yes or No")
game = input()

if game.lower() == "yes":
    capital_game()
    print(f"Welcome to game of matching the State to the Capitals!!")
else:
    print("Ok, next time.  Hope to see you again soon!")
    exit()
