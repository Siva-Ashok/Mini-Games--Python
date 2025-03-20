#guess game

import random

print("guess the game")
secretNumber=random.randint(1,15)

for i in range(6):
    print("take a guess....")
    guess=input()
    guess=int(guess)
    if guess < secretNumber:
          print('guess number is low')
    elif guess==secretNumber:
          print('well done, '+'congratulation,  '+'you guessed my number attempt in '+str(i+1))
          break
    else:
          print('guess number is high')
if guess!= secretNumber:
    print('you lose, '+ 'secret number is  ' +str(secretNumber))
          
      

    

        
    
