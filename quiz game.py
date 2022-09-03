print("WELCOME TO MY QUIZ")
play = input("Do You Want to Play? ")
if play.lower() != "yes":
    quit()
print("OK lets  go")

score = 0

answer = input("what is cc in engines? ")
if answer.lower() == "cubic centimeters":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')

answer = input("what is 'BHP'? ")
if answer.lower() == "break horse power":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')

answer = input("what does 'ABS' stands for? ")
if answer.lower() == "anti lock breaking system":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')

answer = input("what is a halogen? ")
if answer.lower() == "bulb":
    print('CORRECT!')
    score += 1
else:
    print('INCORRECT!')

print ("you answered",score, "questions correctly"  )
