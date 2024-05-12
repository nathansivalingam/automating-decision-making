# Automating Decision Making

## Problem
I wanted to prepare for my upcoming "Mechanics of Solids 2" final exam by completing workshop problems. The final exam could cover all content from weeks 1-10. The workshop questions from each week all consisted of 10 questions. Thus, it seemed like a good idea to randomize the questions in a similar fashion to how they would appear on the test. 

## Solution
I used the "random" library to produce a random week and a random question. This allowed to me to acheive my goal of attempting questions in a manner that would mimic my upcoming exam. Additionally, I added a timer feature which allowed the user to enter how long they expect the question to take them. After that time has passed, a new random question and week is generated. The idea behind this feature was to keep study flowing to avoid the depression that comes with getting stuck for a long time on one problem.

## Operation
1. Open the file in an IDE that supports python.
2. Run the program and enter integer values for the prompts concerning number of questions and number of weeks.
3. After the random question and corresponding week has been generated, enter how long you expect the question to last.
4. After that time has passed, a new question will be generated. Continue this loop until you feel confident :)

## Constraints
The number of weeks must be less than 100.
The number of questions must be less than 100.

## Latest Implementations/Problems
A dictionary is used to keep track of which questions have been completed.
Once all questions have been completed, the program enters an infinite a loop.

There are plans to implement a binary search algorithm somehow, I am not sure yet.