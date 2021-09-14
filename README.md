[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# State Capitals

We're going to create a game to help us memorize the names of the capitals of
all 50 states.

## Prerequisites

- Basics of programming with Python

## Instructions

1. Fork and clone this repository.
1. Change into the new directory.
1. Fulfill the listed requirements.

There is starter code available in `lib/script.py`. Note how the states are
already imported for you!

Write the rest of your code in the `script` file. You can execute a python file
by doing `python3 lib/script.py`

4. When complete, submit your homework by making a pull request on this repository.
Unless otherwise stated, assignments are due the next class day at 10 am ET.

## User Stories

- Provide a welcome message to introduce the player to the game.
- The game will ask the player to enter the capital associated with a given state.
- There should be running tallies on the number of correct and incorrect answers.
- After getting through all 50 states one time, the player should see the final tally (i.e. 45 correct 5 incorrect) and be asked whether or
  not they want to play again.
- If the player enter **`Yes`** it will simply play the game again throughout all State (don't forget to reset the tally)
- If the player enter **`No`** end the game.


**Hint:** It can help to make a copy of the `capitals` list that includes only a
few states for testing purposes.

### Potentially Useful Python Features

- `print()`
- `input()`
- `for` loop
- `sorted()`
- `random.shuffle()`

## Bonus!

- Make sure the states don't appear in alphabetical order in the prompts. This
  will make the game a bit more challenging for the player.
- Initialize **new** keys in the dictionaries that store the number of times a
  player gets a capital `correct` and the number of times the answer is
  `incorrect`.
  - If the answer is correct, display a message saying so, and increment the
    `correct` key.
  - If the answer is incorrect, display a message saying so, and increment the
    `incorrect` key.
- If the player plays again, set the order of how the prompts appear to start with
  the ones they got wrong the most often.
- Add a hint functionality that prints the first 3 letters of a capital

## Plagiarism

Take a moment to refamiliarize yourself with the
[Plagiarism policy](https://git.generalassemb.ly/DC-WDI/Administrative/blob/master/plagiarism.md).
Plagiarized work will not be accepted.
