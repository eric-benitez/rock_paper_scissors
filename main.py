import random


def user_election():
    print('Select')
    for i, element in enumerate(elements):
        print(f'{i + 1} - {element}')
    election = (int(input('Insert your selection: ').strip())) - 1
    return elements[election]


elements = ['rock', 'paper', 'scissors']
cont_user = 0
cont_computer = 0
winner = False
while not winner:
    user = user_election()
    computer = random.choice(elements)

    if user == 'rock' and computer == 'scissors':
        cont_user += 1
    elif user == 'paper' and computer == 'rock':
        cont_user += 1
    elif user == 'scissors' and computer == 'paper':
        cont_user += 1

    if computer == 'rock' and user == 'scissors':
        cont_computer += 1
    elif computer == 'paper' and user == 'rock':
        cont_computer += 1
    elif computer == 'scissors' and user == 'paper':
        cont_computer += 1

    print(f'{cont_user} - {cont_computer}')
    print(f'{user} - {computer}')

    if cont_user >= 3 > cont_computer:
        winner = True
        print('User won')
    elif cont_computer >= 3 > cont_user:
        winner = True
        print('Computer won')

print('User-Computer')
print(f'{cont_user} \t {cont_computer}')
