import random, re

while (True):
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")

    # Get players choice:
    userChoice = input("Choose [R]ock, [P]aper or [S]cissors: ")

    # Check that it's a valid choice:
    if not re.match("[RPS]", userChoice):
        print("That's not a valid choice!")
        continue

    # Confirm user input:
    print("You chose: " + userChoice)

    # Get computer choice
    choices = ['R', 'P', 'S']
    computerChoice = random.choice(choices)

    print("I chose: " + computerChoice)

    # Check for tie
    if userChoice == computerChoice:
        print("It's a tie!")
        continue

    # Check for computer wins
    if computerChoice == 'R' and userChoice == 'S':
        print("Rock beats scissors, I win!")
        continue

    if computerChoice == 'S' and userChoice == 'P':
        print('Scissors beats paper, I win!')
        continue

    if computerChoice == 'P' and userChoice == 'R':
        print('Paper beats rock, I win!')
        continue

    # If computer doesn't win, user does:
    else:
        print("You win!")
        continue

