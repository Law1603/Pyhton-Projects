import random 

user_wins = 0
computer_wins = 0

options = ["rock", "papers", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:").lower()
    if user_input =="q":
        quit()
        
    if user_input  not in ["rock", "paper","scissors"]:     
        continue
    
    random_number = random.randint(0,2)
    # rock: 0, paper:1 , scissors: 2
    
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
       print("You Won!")
       user_wins += 1 
       continue
    
    elif user_input == "rock" and computer_pick == "rock":
       print("You Won!")
       user_wins += 1 
       continue
   
    elif user_input == "rock" and computer_pick == "paper":
       print("You Won!")
       user_wins += 1 
       continue
    else:
       print("You lost")
       computer_wins += 1
       
    print("You won ", user_wins, "times.")
    print("Goodbye!")