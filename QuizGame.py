print(" Welcome To football quiz Game ")
Player = input(" Do you want to play the game? (yes or no)\n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :) ",name_player)

score = 0

answer = input(' UCL in 2022 what team wins \n ')
if answer.lower() == "real mardrid":
    print("Correct")
    score += 1
else:
    print('Wrong')
answer = input(' team2 \n ')
if answer.lower() == 'graphical processing unit':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What is RAM stands for? \n ')
if answer.lower() == 'random access memory':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What is ROM stands for? \n ')
if answer.lower() == 'read only memory':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' Mouse is an input device or output device? \n ')
if answer.lower() == 'input device':
    print("Correct")
    score += 1
else:
    print('Wrong')
    
print("You got the " + str(score)+ " correct answers")
print("You got the " + str((score/5) *100)+ " correct answers")
