from random import choice

# create a list of weeks and a list of questions
weeks = [1, 2, 3, 4, 5, 7, 8, 9, 10]
questions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print a random question from a random week
print(f"MMAN3400: Complete Question {choice(questions)} from Week {choice(weeks)}")