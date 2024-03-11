

import random

def check_win(numbers):
  combinations = [[1, 5, 9], [1, 6, 8], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]]
  for combo in combinations:
    if set(combo).issubset(set(numbers)):
      return True
  return False

def play_game():
  numbers = list(range(1, 10))
  random.shuffle(numbers)
  player1 = []
  player2 = []
  current_player = 1
  game_over = False

  print("Welcome to Number Scrabble!")
  print("The rules are:")
  print("1. The game is played with the list of numbers between 1 and 9.")
  print("2. Each player takes turns picking a number from the list.")
  print("3. Once a number has been picked, it cannot be picked again.")
  print("4. If a player has picked three numbers that add up to 15, that player wins the game.")
  print("5. However, if all the numbers are used and no player gets exactly 15, the game is a draw.")
  print()
  while not game_over:
    print(f"It is player {current_player}'s turn.")
    print(f"The remaining numbers are: {numbers}")
    choice = int(input(f"Player {current_player}, please pick a number from the list: "))

    while choice not in numbers:
      print("Invalid choice. Please pick a number from the list.")
      choice = int(input(f"Player {current_player}, please pick a number from the list: "))
    numbers.remove(choice)
    if current_player == 1:
      player1.append(choice)
    else:
      player2.append(choice)
    print(f"Player {current_player}'s numbers are: {player1 if current_player == 1 else player2}")
    if check_win(player1 if current_player == 1 else player2):
      print(f"Player {current_player} has won the game!")
      game_over = True
    elif len(numbers) == 0:
      print("The game is a draw.")
      game_over = True
    else:
      current_player = 2 if current_player == 1 else 1

play_game()
