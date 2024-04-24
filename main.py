from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high")
    return turns -1
  elif guess < answer:
    print("Too low")
    return turns -1
  else:
    print(f"You got it! The answer was {answer}")


def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  print("Welcome to the Number Guessing Game!")
  print("I\'m thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")
  turns = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("make quess: "))
    turns = check_answer(guess, answer, turns)



game()
# # enimies = 1

# # def increase_enimies():
# #   global enimies
# #   enimies += 1
# #   print(f"enimies inside function: {enimies}")
# #   print(enimies)
# # increase_enimies()

# # print(enimies)

# def bar():
#     my_variable = 9

#     if 16 > 9:
#       my_variable = 16

#     print(my_variable)

# bar()
