from art import logo
from random import randint

player_lives_easy = 10
player_lives_hard = 5
player_guess = 0 

def check_answer(player_guess, computer_number, turns):
  if player_guess < computer_number:
    print("A little to low, maybe try again.")
    return turns - 1
  elif player_guess > computer_number:
    print("A bit over ambitious, you guessed to high. I suggest you try again.")
    return turns - 1
  elif player_guess == computer_number:
    print("CONGRATS, you guessed the correct number. You have won!!!")


def set_difficulty():
  game_level = input("\n\nDo you want to play this game on easy or hard mode?\n\nIf you pick easy you will have 10 guesses and if you pick hard you will only have 5 guesses.\n\nPlease type 'easy' or 'hard' to set your difficulty:  ")
  if game_level == "easy":
    return player_lives_easy
  else:
    return player_lives_hard

computer_number = randint(1, 100)
 
def game(computer_number, player_guess):
  print(logo)
  print("    Welcome to the Number Guessing Game. \n")
  
  turns = set_difficulty()
  player_guess = int(input("What number between 1 - 100 am I thinking of? "))
  
  
  if player_guess == computer_number:
    print(f"You won. You have guessed the correct number {player_guess}")
  elif player_guess > computer_number:
    print("The number you have guessed is too high!")
  elif player_guess < computer_number:
    print("The number you guessed is too low!")


  
  
  while player_guess != computer_number:
    print(f"You have {turns} guesses remaining.")
    player_guess = int(input("What number between 1 - 100 am I thinking of? "))

  

    turns = check_answer(player_guess, computer_number, turns)
    if turns == 0:
      print("You loose. GAME OVER.")
      return
    elif player_guess == computer_number:
        return
    elif turns != 0:
      print("Guess again: ")

game(computer_number, player_guess)
