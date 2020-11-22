import random

def gamewin(you,comp):
    if you == comp:
        return None

    if you == 's':
        if comp== 'w':
            return True
        elif comp =='g':
            return False
    elif you == 'w':
        if comp== 's':
            return False
        elif comp=='g':
            return True
    elif you== 'g':
        if comp== 'w':
            return False
        elif comp =='s':
            return True  

randNUM=random.randint(1,3)#random module is used
print('computers turn: snake(s) water(w) gun(g)')

you=input('enter your turn  ')

if randNUM==1:
    comp = 's'
elif randNUM==2:
    comp='w'
elif randNUM==3:
    comp='g'

print(f'computerchoosed:{comp}')    #to display what computer has choosen

nikhilgame=gamewin(you,comp)
if nikhilgame==None:
    print('its a tie')
elif nikhilgame==True:
    print('You won')
elif nikhilgame==False:
    print('better luck next time')
