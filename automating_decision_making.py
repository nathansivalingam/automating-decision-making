from random import randint
from time import sleep

# input find the number of weeks and number of questions
print("Enter Number of Weeks: ", end="")
num_weeks = int(input())
print("Enter Number of Questions: ", end="")
num_questions = int(input())

# initialise all questions as incomplete
my_dict = {}
for i in range(1, num_weeks + 1):
    for j in range(1, num_questions + 1):
        key = "{:02d}".format(i) + "{:02d}".format(j)
        my_dict[key] = "incomplete"

count = 0
# print a random question from a random week
while True:
    cur_question = randint(1, num_questions)
    cur_week = randint(1, num_weeks)
    key = "{:02d}".format(cur_question) + "{:02d}".format(cur_week)

    # if question has already been completed, generate a new question
    if count == (num_weeks * num_questions):
        print("ALL QUESTIONS COMPLETED")
        break
    elif my_dict[key] == "complete":
        count+=1
        continue
    else:
        print(f"MMAN3400: Complete Question {cur_question} from Week {cur_week}")
        print(f"Expected time to complete question [minutes]: ", end="")
        dur = int(input())
        sleep(dur * 60 * 0)

        # checks whether the question has been completed
        print("Has the question been completed? (yes|no) ", end="")
        completed_status = str(input())
        if completed_status == "yes":
            my_dict[key] = "complete"
        elif completed_status == "no":
            my_dict[key] = "attempted"