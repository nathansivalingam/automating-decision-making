# Automating Decision Making

## Problem
I wanted to prepare for my upcoming "Mechanics of Solids 2" final exam by completing workshop problems. The final exam could cover all content from weeks 1-10. The workshop questions from each week all consisted of 10 questions. Thus, it seemed like a good idea to randomize the questions in a similar fashion to how they would appear on the test. Gamifying the process also makes studying more fun. This is also a form of procrastination. 

## Solution
I used the "random" library to produce a random week and a random question. This allowed to me to acheive my goal of attempting questions in a manner that would mimic my upcoming exam. 

Additionally, I added a timer feature which allowed the user to enter how long they expect the question to take them. After that time has passed, a new random question and week is generated. The idea behind this feature was to keep study flowing to avoid the depression that comes with getting stuck for a long time on one problem. 

I stored the questions in a dictionary with a status that is either (incomplete|complete|attempted). Incomplete and attempted questions get cycled until all questions are completed. Once all questions are marked as complete, the program finishes.

## Operation
1. Open the file in an IDE that supports python.
2. Run the program and enter integer values for the prompts concerning number of questions and number of weeks.
3. After the random question and corresponding week has been generated, enter how long you expect the question to last.
4. After that time has passed, a new question will be generated. Continue this loop until you feel confident or until all the questions have passed :)

## Constraints
The number of weeks must be less than 100. [Not super sure why tho]
The number of questions must be less than 100 [ditto].

## Latest Implementations/Problems
There are plans to implement a binary search algorithm somehow, I am not sure yet.
I would like to implement a front end, that displays the questions as squares. The squares follow the key:
- Incomplete = Red or Default Grey
- Attempted = Yellow
- Complete = Green
Maybe a cool animation follows the completion of a question, not super sure tho.