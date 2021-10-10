import random

def play():
    user=input("give imput r or p or s ")
    computer = random.choice(['r','p','s'])
    print(computer)



    if(user==computer):
        return 'tie'


    if win (user , computer):
        return 'you won'

     
    return 'you lost '

def win(player, oponent):
    if (player== 'r' and oponent== 's') or (player=='s' and oponent=='p') or (play=='p'or oponent=='r'):
     return True

print(play())