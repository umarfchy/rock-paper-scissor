#!/usr/bin/env python
# coding: utf-8

# # The 'Rock Paper Scissor'

# ## objective of the game is to make 10 points 
# ## whoever makes 10 points first will win the game
# ## the game is between a player and computer

# 
# 
# # Function to generate computer's choice

# In[1]:


def decide():
    import random
    choice = ['Rock', 'Paper', 'Scissor']
    return choice[random.randint(0,2)]


# # Funtion to Compare between player's and computer's choices

# In[2]:


def compare(playerChoice, computerChoice):
    
    playerChoice = playerChoice.capitalize()

    if playerChoice in ['Rock', 'Paper', 'Scissor']:
        
        if playerChoice == computerChoice:
            return 2

        elif playerChoice == 'Rock' and computerChoice == 'Paper':
            return 0    

        elif playerChoice == 'Rock' and computerChoice == 'Scissor':
            return 1
             
        elif playerChoice == 'Scissor' and computerChoice == 'Paper':
            return 1

        elif playerChoice == 'Scissor' and computerChoice == 'Rock':
            return 0
             
        elif playerChoice == 'Paper' and computerChoice == 'Rock':
            return 0

        elif playerChoice == 'Paper' and computerChoice == 'Scissor':
            return 1

    else:
        pass


# # Function to return score and prints who wins

# In[ ]:


def scoreCounter(value,point):
    if value == 0:
        points['computer'] +=1
        print('\n Computer Wins')
    elif value == 1:
        points['player'] +=1
        print('\n You Win') 
    elif value == 2:
        print("\nIt's a draw. Both of you chose", playerChoice)
    else:
        print('*'*100)
        print('\nPlease give a valid input. Your input must be among Rock, Paper, Scissor')
        print("*"*100)


# # Program Body

# In[ ]:


print('Welcome to "Rock Paper Scissor" ')

#Dictionary that counts and stores points
points = {
    'player' : 0, 
    'computer': 0
}

while points['computer'] != 10 or points['computer'] != 10:
    
    #inputs from player and computer
    playerChoice = input('Give you choice. Keep your choice among Rock, Paper and Scissor : \n')
    computerChoice = decide()
    
    #compares the choices between player and computer
    comparison = compare(playerChoice, computerChoice)
    
    scoreCounter(value = comparison, point = points)    
            
    print('\nYour Choice : ', playerChoice, '\nComputer\'s Choice : ', computerChoice)
    print('\n\nYour Score\t: ', points['player'] , '\nCompute\'s Score : ', points['computer'])
    print('-'*100)
    

if points['computer'] == 10:
    print('\n\nSorry, You lose the game')
else:
    print('\n\nCongratulations, You won the game')

