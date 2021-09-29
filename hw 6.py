import random
#Rock Paper Scissors

#Step 1/2, tell the rules/Give them their choices
def intro():
    print("===================================")
    print("============== RULES ===============")
    print("Welcome to Rock,Paper,Scissors!")
    print("Select Rock, Paper, Scissors")
    print("Rock beats Scissors, and Lizard")
    print("Scissors beats Paper, and Lizard")
    print("Paper beats Rock, and Spock")
    print("lizard beats paper and spock")
    print("Spock beats scissors and rock")
intro()
#Step 3, players choose their move
def Player():
    print("==================================================")
    print("================== PLAYER TURN =====================")
    print("Type Rock, Paper, Scissors,Lizard, or Spock")
    temp = input("please select your option >>")
    while temp.lower() != "rock" and temp.lower() != "scissors" and temp.lower() != "paper" and temp.lower() != "lizard" and temp.lower() != "spock":
        temp = input("Invalid choice, try again >>")

    print("====================================================")
    return temp

def Cpu():
    return random.choice(["rock","paper","scissors","lizard","spock"])
    #.33 or 1/3
#generate a random number between 0 and 100
#if the CPU chooses between 0-32 it's rock
#if cpu chooses between 33-62 it's paper
#if cpu chooses between 63-100 it's scissors



gameOver = None
Playerscore = 0
CPUscore = 0
while gameOver != "n":
    playerChoice = Player()
    cpuChoice = Cpu()

    # Step 4, Players show their choices
    print("================ RESULTS ===================")
    print("Player choice: " + playerChoice)
    print("CPU choice: " + cpuChoice)

    # Step 5, Result of the match is determined
    if playerChoice == cpuChoice:
        print("Player and Cpu has tied!")
    elif playerChoice == "rock":
        if cpuChoice == "scissors" or "lizard":
            print("Player has won with rock!")
            Playerscore += 1
        else:
            print("CPU has won with " + cpuChoice)
            CPUscore += 1
    elif playerChoice == "scissors":
        if cpuChoice == "paper" or "lizard":
            print("Player has won with scissors!")
            Playerscore += 1
        else:
            print("CPU has won with " + cpuChoice)
            CPUscore += 1
    elif playerChoice == "paper":
        if cpuChoice == "rock" or "spock":
            print("Player has won with paper!")
            Playerscore += 1
        else:
            print("CPU has won with " + cpuChoice)
            CPUscore += 1
    elif playerChoice == "lizard":
        if cpuChoice == "spock" or "paper":
            print("Player has won with lizard!!")
            Playerscore += 1
        else:
            print("CPU won with " + cpuChoice)
            CPUscore += 1
    elif playerChoice == "spock":
        if cpuChoice == "scissors" or "rock":
            print("player has won with spock!!")
            Playerscore += 1
        else:
            print("CPU has won with " + cpuChoice)
            CPUscore += 1
    print("Player score is " + str(Playerscore))
    print("CPU score is " + str(CPUscore))
    gameOver = input("do you want to play again? Type 'y' or 'n'")