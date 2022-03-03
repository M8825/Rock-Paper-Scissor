from random import choice


user_name = input('Enter your name:')
print(f'Hello, {user_name}')

file = open('rating.txt', 'r')
score = 0

for line in file:
    name = line.split()
    if name[0] == user_name:
        score = int(name[1])
        break
file.close()

# Get new game options list from user
game_options = input()
if not game_options:  # Assign default options
    game_options = ['rock', 'paper', 'scissors']
else:
    game_options = game_options.split(',')

print("Okay, let's start")
while True:
    usr_inp = input()

    if usr_inp == '!exit':
        print('Buy!')
        break
    elif usr_inp == '!rating':
        print(f'Your rating: {score}')
        continue
    elif usr_inp not in game_options:
        print('Invalid input')
        continue

    comp_choice = choice(game_options)
    user_opt = game_options.index(usr_inp)  # Get option index in original list
    new_options = game_options[user_opt + 1:] + game_options[:user_opt]
    winners = new_options[:int(len(new_options) / 2)]

    if comp_choice == usr_inp:
        print(f'There is a draw ({comp_choice})')
        score += 50
    elif comp_choice in winners:
        print(f'Sorry, but the computer chose {comp_choice}')
    else:
        print(f'Well done. The computer chose {comp_choice} and failed')
        score += 100