
# coding: utf-8

# In[1]:


from IPython.display import clear_output
from time import sleep

player1 = None
player2 = None
times = 1
player1_turn = True
input_dict = {'p1':[], 'p2':[]}

def wanna_play():
    global player1
    global player2
    global times

    if times == 1:
        print("Welcome to Tic Tac Toe")
        player1 = ask_X_or_O_for_player1()
        player2 = set_player2(player1)
    else:
        switch_player_position()
         
    times += 1
    
    return valid_input()

def ask_X_or_O_for_player1():
    while True:
        player1 = input("Player 1: Do you want to be X or O\n").upper()
        if player1 in "OX":
            return player1

def set_player2(player1):
    if player1 == "X":
        return "O"

    return "X"

def switch_player_position():
    global player1
    global player2
    if player1 == "X":
        player1 = "O"
        player2 = "X"
    else:
        player1 = "X"
        player2 = "O"

def valid_input():
    while True:
        choice = input("Are you ready to play. Enter Yes or No\n").lower()
        if choice == "yes":
            print("Player 1 will go first")
            return True
        elif choice == "no":
            return False
        else:
            print("Please enter Yes or No")
    


# In[2]:


def change_player_turn():
    global player1_turn
    if player1_turn:
        player1_turn = False
    else:
        player1_turn = True

def valid_input_pos():
    
    global input_dict
    while True:
        input_pos = int(input("Choose your next position 1-9"))
        for input_so_far in input_dict.values():
            if input_pos in input_so_far:
                print("Invalid position specified")
            elif player1_turn:
                input_dict['p1'].append(input_pos)
                return
            else:
                input_dict['p2'].append(input_pos)
                return
    


# In[3]:


def display_board():

    #input_dict is global
    component = {"empty": "     |     |     \n", "border":"-----------------\n", 0: "  {}  |  {}  |  {}  \n"}
    
    p1_p2_lists = input_dict.values()
    #Will return 2 arrays which we have to join
    
    mega_list = []
    
    for l in p1_p2_lists:
        mega_list += l
    #They are joined by above for loop
    
    mega_list.sort() #Now we sort is because I want to insert " " inside
    
    for i in range(9):
        if i + 1 not in mega_list:
            mega_list.insert(i, " ")
        else:
            if i + 1 in input_dict['p1']:
                mega_list[i] = player1
            else:
                mega_list[i] = player2

    # Inserted " " in the place where there isn't a number
    
    #Now printing the tic tac toe with X and O's
    #In the format 
    # 7 8 9
    # 4 5 6
    # 1 2 3
    i = 2
    while i > -1:
        print(component["empty"])
        j = i * 3
        
        print(component[0].format(mega_list[j], mega_list[j + 1], mega_list[j + 2]))
        print(component["empty"])
        
        if i != 0:
            print(component["border"])
        i -= 1
        
def reset_input_dict():
    global input_dict
    for key in input_dict.keys():
            input_dict[key] = []
    


# ### 

# In[4]:


def main_loop():
    total_inputs = 0
    while wanna_play():
        # WE need to keep track of the places where what has gone
        
        while total_inputs < 9:
                clear_output()
                
                display_board()
                
                valid_input_pos()
                
                total_inputs += 1
                change_player_turn()
             
        display_board()
        reset_input_dict()
        
        total_inputs = 0
        clear_output()
            
main_loop()
            

