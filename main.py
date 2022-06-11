import random

print("The Rules for this game: \n"
      +"Rock beats Scissors 💥 \n"
      +"Paper beats Rock 💥 \n"
      +"Scissors beats Paper 💥 \n")

print("R for Rock \n"
      +"P for Paper \n" 
      +"S for Scissors")

#creating a list to store all possible options
l = ["R", "P", "S"]

def re_run():
    player_option()
    computer_option()
    check_winner()


def player_option():
    print ("Enter Your Choice Please \n 1 for Rock, \n 2 for Paper, and \n 3 for Scissors \n")
    
    #Collecting User's Input
    choice = int(input("Player's turn: "))
    while choice > 3 or choice < 1:
        choice = (input("Invalid option, Kindly enter valid input: "))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    elif choice == 3:
        choice_name = 'Scissors'
    print('User Choice is: ' + choice_name)
    player_option.choice = choice
    player_option.player_choice = choice_name
player_option()

print("\n Computer's Turn")

def computer_option():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'Paper'
    elif computer_choice == 3:
        computer_choice_name = 'Scissors'

    print("Computer choice is: "+ computer_choice_name)
    computer_option.choice = computer_choice
    computer_option.computer_choice = computer_choice_name
computer_option()

print("Player(",player_option.player_choice,")", ":" ,"CPU (", computer_option.computer_choice, ")")

def check_winner():
    if((player_option.choice == 1 and computer_option.choice == 2) or (player_option.choice == 2 and computer_option.choice == 1)):
        print("Paper wins =>", end = "")
        check_winner.result = 'Paper'
    
    elif((player_option.choice == 1 and computer_option.choice == 3) or (player_option.choice == 3 and computer_option.choice == 1)):
        print("Rock wins =>", end = "")
        check_winner.result = 'Rock'
        
    elif((player_option.choice == 3 and computer_option.choice == 2) or (player_option.choice == 2 and computer_option.choice == 3)):
        print("Scissors wins =>", end = "")
        check_winner.result = 'Scissors'
    
    elif((player_option.choice == computer_option.choice)):
        print("Its a Tie")
        re_run()
        
check_winner()

# Printing either user or computer wins
def print_result():
    if check_winner.result == player_option.player_choice:
        print('💥User Wins💥')
    else:
        print('💥Computer Wins💥')
print_result()

print("Do you want to go again?? (Y/N)")
answer = input()
    
if answer == 'n' or answer == 'N':
    print("\nThanks for playing")
else:
    re_run()