import random as rand

 
def play():
    user = input("Hey there i am AI are you ready to play rock, paper, scissor with me,\
\nNow let's get started,\
\nWhat's your choice? \n").lower()
    comp = rand.choice(['Rock', 'Paper', 'Scissor']).lower()
    print(f"Computer chooses: {comp.capitalize()}")
    if user == comp:
       return "Tie"
    if us_win(user, comp):
        return "You won!"
    else:
        return "You lost!" 
    
def us_win(you, opp):
        if (you == "paper" and opp == "rock") or (you == "scissor" and opp == "paper") \
or (you == "rock" and opp == "scissor"):
            return True
        
print(play())

