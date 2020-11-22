import random
number= random.randint(1,10000)     #generates a radnom number between given limits
# print(number)                     #use this if you cant find the ranom number
userguess= None
guess = 0

while userguess!= number:                       # loop to count number of guesses 
    userguess=int(input('enter your guess :'))
    guess= guess+1                              #increment after each guess
    if userguess == number:
        print(' you got it right')
    elif userguess>number:
        print('smaller number pls')
    elif userguess<number:
        print('larger num pls')      
print(f'you have guessed in just {guess} guesses')

with open('highscore.txt','r') as f:            #opening the highscore text file and reading value as int
    num= int(f.read())
if guess< num:
    print('you broke the record')
    with open ('highscore.txt', 'w') as f:          #writing into highscore.txt
        f.write(str(guess)) 
elif guess==num:
    print('you have equaled the high score')         
else:
    print('you didnt make into the highscore board')       


