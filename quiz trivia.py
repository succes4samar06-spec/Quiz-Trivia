name=input("Enter your name: ")
print("welcome", name)

score=0

print(" RULES OF THE GAME ARE AS FOLLOWS:")
print("+1 for each correct answer")
print("-1 for each wrong answer")

Q1= input("Q1. what is the colour of sun's UV rays ?").lower()
if Q1== "white":
    print(" Congratulations! your answer is correct")
    score = score +1
else:
    print("wrong!")
    score = score -1

Q2= input("Q2. which planet is known as the red plant ?").lower()
if Q2=="mars":
    print(" Congratulations! your answer is correct")
    score = score +1
else:
    print("wrong!")
    score = score -1



Q3= input("Q3. Name the national animal of India ?").lower()
if Q3=="tiger":
    print("Congratulations! your answer is correct")
    score = score +1
else:
    print("wrong!")
    score = score -1


Q4= input("Q4. Which is the heaviest animal on the world ?").lower()
if Q4=="blue whale":
    print(" Congratulations! your answer is correct")
    score = score +1
else:
    print("wrong!")
    score = score -1


Q5= input("Q5. Which mathematician is known as the human calculator?").lower()
if Q5=="Shakuntla Devi":
    print("Congratulations! your answer is correct")
    score = score +1
else:
    print("wrong!")
    score = score -1

print("QUIZ OVER")
print("your final score is", score)
if score== 5:
    print("excellent!")
elif score>= 3:
    print("good job!")
else:
    print("better luck next time!")

print("Thank you for being the part of trivia quiz")