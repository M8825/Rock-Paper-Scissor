from random import choice

user_name = input('Enter your name:')
print(f'Hello, {user_name}')

file = open('rating.txt', 'r')

score = 0

for line in file:
    name = line.split()
    if name[0] == user_name:
        score = int(name[1])

while True:
    comp_choice = choice(['rock', 'paper', 'scissors'])
    comp_win_opts = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}

    usr_inp = input()

    if usr_inp == '!exit':
        print('Buy!')
        break
    elif usr_inp == '!rating':
        print(f'Your rating: {score}')
        continue
    elif usr_inp not in comp_win_opts:
        print('Invalid input')
        continue

    option = comp_win_opts[usr_inp]

    if comp_choice == usr_inp:
        print(f'There is a draw ({comp_choice})')
        score += 50
    elif option == comp_choice:
        print(f'Sorry, but the computer chose {comp_choice}')
    else:
        print(f'Well done. The computer chose {comp_choice} and failed')
        score += 100