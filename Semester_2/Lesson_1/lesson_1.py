from data import questions

user_results = []
user_points = 0

# Test explanation
print(
    f"Hello there!\nInput correct answer, for skip questions use button 'E' with upper case.\nThere are some GPT system requirements:\n"
    f"\n\tA - greater than 86%\n\tB - greater than 75%\n\tC - greater than 65%\n\tFor F - less than 65%.\n\t\t\t\tGood Luck!"
)

# Itering question for test user
for question, val in questions.items():
    new_question = input(f"\n{question} \n")

    if new_question == val:
        user_results.append("correct")
        user_points += 1
    elif new_question == "E":
        user_results.append("skipped")
        user_points += 0
    else:
        user_results.append("incorrect")
        user_points += 0

percent = abs(user_points * (100 / len(questions)))

"""GPA system"""
if percent > 86:
    gpa_system = "A"
elif 75 < percent < 86:
    gpa_system = "B"
elif 65 < percent < 75:
    gpa_system = "C"
else:
    gpa_system = "F"


# Output
print(
    "|------------------------------------|\n"
    f"|**********TEST-RESULTf**********|"
    f"\nYour correct answers: {user_results.count('correct')}."
    f"\nIncorrect answers: {user_results.count('incorrect')}."
    f"\nOverall percentage: {percent:.2f}% .\n"
)

for index, answer in enumerate(user_results, 1):
    print(f"{index} question was {answer}!")
