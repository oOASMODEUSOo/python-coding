from random import randint, random

Option_dictionary={1:"Rock",
                    2:"Paper",
                    3:"Scissors"}

# print(Option_dictionary[2])


round_count = int(input("How many rounds do you want: "))

# User_input = int(input('Enter your choice 1:Rock, 2:Paper, 3:Scissors; '))

i=1

# print(User_input, CPU_input)

def win_cond(User_input, CPU_input, User_Wins, CPU_Wins):
    if Option_dictionary[User_input] == "Rock" and Option_dictionary[CPU_input]== "Paper":
        print("CPU wins this round")
        CPU_Wins+=1

    elif Option_dictionary[User_input] == "Rock" and Option_dictionary[CPU_input]== "Scissors":
        print("User wins this round")
        User_Wins+=1
    
    elif Option_dictionary[User_input] == "Paper" and Option_dictionary[CPU_input]== "Rock":
        print("User wins this round")
        User_Wins+=1
    
    elif Option_dictionary[User_input] == "Paper" and Option_dictionary[CPU_input]== "Scissors":
        print("CPU wins this round")
        CPU_Wins+=1

    elif Option_dictionary[User_input] == "Scissors" and Option_dictionary[CPU_input]== "Rock":
        print("CPU wins this round")
        CPU_Wins+=1

    elif Option_dictionary[User_input] == "Scissors" and Option_dictionary[CPU_input]== "Paper":
        print("User wins this round")
        User_Wins+=1

    else:
        print("It's a DRAW")
    
    return User_Wins, CPU_Wins


User_Wins = 0
CPU_Wins = 0
round_check = round_count
while i <=round_count:

    # round_check = round_count

    round_to_win = round_check//2 + 1

    User_input = int(input('Enter your choice 1:Rock, 2:Paper, 3:Scissors; '))
    CPU_input = randint(1,3)
    User_win, CPU_win = win_cond(User_input, CPU_input, User_Wins, CPU_Wins)

    print(User_win, CPU_win, "\n")

    if User_win == round_to_win:
        print('User wins')
        break

    elif CPU_win == round_to_win:
        print("CPU wins")
        break
    
    else:
        round_count+=1

    i+=1
    CPU_Wins = CPU_win
    User_Wins = User_win

