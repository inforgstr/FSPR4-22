from data import questions
import csv

user_results = []
user_points = 0

# Test explanation
print(
    f"Hello there!\nInput correct answer, for skip questions use button 'E' with upper case.\nThere are some GPT system requirements:\n"
    f"\n\tA - greater than 86%\n\tB - greater than 75%\n\tC - greater than 65%\n\tFor F - less than 65%.\n\t\t\t\t\t\t\tGood Luck!"
)

# Itering question for test user
if questions:
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

percent = user_points * (100 / len(questions))
incorrects = user_results.count("incorrect") + user_results.count("skipped")

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
result = [
    "\t\t\t|--------------------------------|",
    "\t\t\t|**********TEST-RESULTS**********|",
    f"\t\t\tCorrect answers: {user_results.count('correct')}.",
    f"\t\t\tIncorrect answers: {incorrects}.",
    f"\t\t\tOverall percentage: {percent:.2f}% .",
    f"\t\t\tYour GPA score is {gpa_system}",
    f"\t\t\t__________________________________\n\n\n",
]
text = result + [
    f"\t\t\t\t{index} answer was {answer}"
    for index, answer in enumerate(user_results, 1)
]

with open("Semester_2/Lesson_1/file.csv", "w", newline="") as file:
    csv_writer = csv.writer(file, delimiter="\n")
    csv_writer.writerow(text)
