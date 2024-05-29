import random


# Checks whether user enters yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # Checks users response, question.
        # Repeats if users don't enter yes / no.
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no.")


# instructions
def instruction():
    print('''
    **** Instructions ****

You will be provided with 4 operations.
select which operations you would like in your quiz.
Try to answer the questions correctly.

Good Luck & Have Fun!
    ''')


# operation options for user to select (addition, subtraction, multiplication, division)
def addition():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    answer = num_1 + num_2
    question = f"What is {num_1} + {num_2}? \n"
    return question, answer


def subtraction():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, num_1)
    answer = num_1 - num_2
    question = f"What is {num_1} - {num_2}? \n"
    return question, answer


def multiplication():
    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)
    answer = num_1 * num_2
    question = f"What is {num_1} x {num_2}? \n"
    return question, answer


def division():
    num_2 = random.randint(1, 12)
    answer = random.randint(1, 12)
    num_1 = num_2 * answer
    question = f"What is {num_1} ➗ {num_2}? \n"
    return question, answer


# initialising variables
correct_answers = 0
incorrect_answers = 0
questions_answered = 0
operations = []
game_history = []

# main routine begins
print()
print("Welcome to my math quiz!")
print()

# displays instructions to user
want_instructions = yes_no("Do you want to read the instructions? ")
if want_instructions == "yes":
    instruction()


# displays all operation options
want_addition = yes_no("Would you like to use addition in your quiz? ")
if want_addition == "yes":
    operations.append(addition)
    print("You will get addition questions.")
    print()
elif want_addition == "no":
    print("Your quiz will not include addition.")
    print()


want_subtraction = yes_no("Would you like to use subtraction in your quiz? ")
if want_subtraction == "yes":
    operations.append(subtraction)
    print("You will get subtraction questions.")
    print()
elif want_subtraction == "no":
    print("Your quiz will not include subtraction.")
    print()


want_multiplication = yes_no("Would you like to use multiplication in your quiz? ")
if want_multiplication == "yes":
    operations.append(multiplication)
    print("You will get multiplication questions.")
    print()
elif want_multiplication == "no":
    print("Your quiz will not include multiplication.")
    print()


want_division = yes_no("Would you like to use division in your quiz? ")
if want_division == "yes":
    operations.append(division)
    print("You will get division questions.")
    print()
elif want_division == "no":
    print("Your quiz will not include division.")
    print()

# if you don't choose any operations, end the quiz.
if not operations:
    print("You have not chosen any operations. Ending quiz now.")

# creates loop
else:
    while True:
        questions = int(input("How many questions would you like to answer? "))

        if questions <= 0:  # user cannot do a quiz without questions, end quiz if user chooses 0 questions.
            print("You can't do a quiz without questions! (ending quiz)")
            break

        # if questions chosen is greater than 0, start the quiz.
        if questions > 0:
            print("We're gonna start the quiz! ")

            for _ in range(questions):
                operation = random.choice(operations)  # selects a random operation from the operations you chose
                question, answer = operation()  # selects a question and an answer for the operation

                # prints heading for each question.
                heading = f"\n Question {questions_answered + 1}"
                print(heading)

                # asks question and gets users response
                user_response = int(input(question))

                # checks if user got the question correct
                if user_response == answer:
                    questions_answered += 1
                    print("You got it right! ")
                    correct_answers += 1
                    history_item = f" Question: {questions_answered}: Your answer of {answer} was correct!"
                    game_history.append(history_item)

                    # if user didn't get it right, they got it wrong.
                else:
                    questions_answered += 1
                    print(f"Sorry, that's incorrect, the correct answer was {answer} ")
                    incorrect_answers += 1
                    history_item = f" Question: {questions_answered}: Sorry that was incorrect," \
                                   f" the correct answer was {answer}"
                    game_history.append(history_item)

            # Asks if user would like to see quiz results.
            results = yes_no("Quiz complete! Would you like to see your results? ")
            if results == "yes":
                print(f"You got {correct_answers} questions correct and {incorrect_answers} questions incorrect. ")

            # asks if user wants to see game history and if they do print game history.
            if questions_answered > 0:
                see_history = yes_no("Do you want to see your quiz history? ")

                if see_history == "yes":
                    print("Game History: ")

                    for item in game_history:
                        print(item)
                        