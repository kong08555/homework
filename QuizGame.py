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
answer = input('who is most assists in premier league\n (trent alexander arnold, harry kane, kevin de bryne, mohamed salah, mason mount) \n ')
if answer.lower() == 'mohamed salah':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' how many goals does karim benzema score in UCL\n(17, 15, 20, 18, 14) \n ')
if answer.lower() == '15':
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
