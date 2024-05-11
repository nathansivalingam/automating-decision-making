from random import randint
from time import sleep

# input find the number of weeks and number of questions
print("Number of Weeks: ", end="")
weeks = int(input())
print("Number of Questions: ", end="")
questions = int(input())

# print a random question from a random week
while True:
    print(f"MMAN3400: Complete Question {randint(1, questions)} from Week {randint(1, weeks)}")
    print(f"Expected time to complete question [minutes]: ", end="")
    dur = int(input())
    sleep(dur * 60)