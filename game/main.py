import random

# Function choose_options

def choose_options():
  options = ('paper', 'rock', 'scissor')
  user_option = input('rock, paper or scissor => ').lower()
  if not user_option in options:
    print('That\'s not a valid option')
    return None
  computer_option = random.choice(options)
  return user_option, computer_option

# rules function

def check_rules(user_option, computer_option, user_wins, pc_wins):
  if user_option == computer_option:
    print('Draw, no points will be given.')
  elif user_option == 'paper':
    if computer_option == 'rock':
      user_wins += 1
    else:     
      pc_wins += 1
  elif user_option == 'scissor':
    if computer_option == 'paper':
      user_wins += 1
    else:
      pc_wins += 1
      print('It has a rock')
  elif user_option == 'rock':
    if computer_option == 'scissor':
      user_wins += 1
    else:
      pc_wins += 1
  else:
    print('That\'s not a valid option')
  return user_wins, pc_wins

    
    

# main function

def run_games():
  round = 1
  user_wins = 0
  pc_wins = 0

  while True:
    
    print('*' * 10)
    print('ROUND:', round)
    print('*' * 10)

    print('Computer wins: ', pc_wins)
    print('User wins: ', user_wins)
    round += 1

    user_option, computer_option = choose_options()
    user_wins, pc_wins = check_rules(user_option, computer_option, user_wins, pc_wins)


    if user_wins == 2:
      print('User wins!!!')
      break
    if pc_wins == 2:
      print('Computer wins!!!')
      break
    else:
      continue
  

run_games()

 
  
