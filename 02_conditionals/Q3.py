# Problem: Assign a letter grade based on a student's score:
#  A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter your score: "))

if(score > 100 or score < 0):
    print("score must be provided between 0 - 100")
    exit()
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade based on your score is: {}".format(grade))