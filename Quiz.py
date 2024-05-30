import random   # allows random numbers


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


# instructions function
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
    num_1 = random.randint(0, 100)  # generates random numbers from 0 - 100
    num_2 = random.randint(0, 100)  # generates random numbers from 0 - 100
    answer = num_1 + num_2          # Answer will be first number + second number.
    question = f"What is {num_1} + {num_2}? \n"    # Creates question that user will answer
    return question, answer         # returns question and answer for user


def subtraction():
    num_1 = random.randint(0, 100)      # generates random numbers from 0 - 100
    num_2 = random.randint(0, num_1)    # Generates random number between 0 and first number (so answer isn't negative)
    answer = num_1 - num_2              # answer will be first number minus second number.
    question = f"What is {num_1} - {num_2}? \n"    # creates question that user will answer
    return question, answer             # returns question and answer for user


def multiplication():
    num_1 = random.randint(1, 12)   # generates random numbers from 1 - 12
    num_2 = random.randint(1, 12)   # generates random numbers from 1 - 12
    answer = num_1 * num_2          # answer is first number multiplied by second number
    question = f"What is {num_1} x {num_2}? \n"    # creates question that user will answer
    return question, answer         # returns question and answer for user


def division():
    num_2 = random.randint(1, 12)   # second number will be a number between 1 and 12
    answer = random.randint(1, 12)  # answer is a number between 1 and 12
    num_1 = num_2 * answer  # first number will be second number multiplied by answers number. (stops decimal answers)
    question = f"What is {num_1} ➗ {num_2}? \n"    # creates question that user will answer
    return question, answer         # returns question and answer for user


# initialising variables
questions_answered = 0
operations = []
game_history = []

# main routine begins
print()
print("Welcome to my math quiz!")
print()

# Calls instructions function and asks the user if they would like to read the instructions
want_instructions = yes_no("Do you want to read the instructions? ")

# if user enters "yes" instructions will be displayed to the user
if want_instructions == "yes":
    instruction()


# displays all operation options from their functions for user to select.
want_addition = yes_no("Would you like to use addition in your quiz? ")
if want_addition == "yes":  # Calls Addition function if user replies with "yes"
    operations.append(addition)
    print("You will get addition questions.")
    print()
elif want_addition == "no":    # Ignores addition function if user replies with "no"
    print("Your quiz will not include addition.")
    print()


want_subtraction = yes_no("Would you like to use subtraction in your quiz? ")
if want_subtraction == "yes":   # Calls subtraction function if user replies with "yes"
    operations.append(subtraction)
    print("You will get subtraction questions.")
    print()
elif want_subtraction == "no":    # Ignores subtraction function if user replies with "no"
    print("Your quiz will not include subtraction.")
    print()


want_multiplication = yes_no("Would you like to use multiplication in your quiz? ")
if want_multiplication == "yes":    # Calls multiplication function if user replies with "yes"
    operations.append(multiplication)
    print("You will get multiplication questions.")
    print()
elif want_multiplication == "no":   # Ignores multiplication function if user replies with "no"
    print("Your quiz will not include multiplication.")
    print()


want_division = yes_no("Would you like to use division in your quiz? ")
if want_division == "yes":  # Calls division function if user replies with "yes"
    operations.append(division)
    print("You will get division questions.")
    print()
elif want_division == "no":    # Ignores division function if user replies with "no"
    print("Your quiz will not include division.")
    print()

# if you don't choose any operations, end the quiz.
if not operations:
    print("You have not chosen any operations. Ending quiz now.")

# creates loop
else:
    while True:
        # asks user how many questions they want to answer
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
                    history_item = f"Question {questions_answered}: {question} Your answer of {answer} was correct!"
                    game_history.append(history_item)

                    # if user didn't get it right, they got it wrong.
                else:
                    questions_answered += 1
                    print(f"Sorry, that's incorrect, the correct answer was {answer} ")
                    history_item = f"Question {questions_answered}: {question} Sorry, {user_response} was incorrect," \
                                   f" the correct answer was {answer}"
                    game_history.append(history_item)

            # asks if user wants to see quiz history and if they do print quiz history.
            if questions_answered > 0:
                see_history = yes_no("Do you want to see your quiz history? ")

                if see_history == "yes":    # if user responds "yes" print quiz history
                    print("Quiz History: ")

                    for item in game_history:
                        print(item)
            break   # ends the loop and quiz
