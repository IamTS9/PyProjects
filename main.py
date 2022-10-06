from logo import logo
import requests
import bs4
from random import choice
# Web Scraping
result = requests.get('https://www.sacnilk.com/articles/internet/instagram/List_of_MostFollowed_Instagram_Handle_in_World?hl=en')
soup = bs4.BeautifulSoup(result.text, 'lxml')
x = soup.select('.table1')

data = x[0].text.split('\n')

# print(data)
del data[0:4]
new_data = []
for i in data:
    if i != '':
        new_data.append(i)

# print(new_data)


# print('Guess who has more instagram followers: ')
org_data_name = []
for i in range(1, 538, 6):
    org_data_name.append(new_data[i])

# print(org_data_name)

org_data_followers = []
for i in range(2, 539, 6):
    org_data_followers.append(new_data[i])

# print(org_data_followers)

# Gameplay
points = 0
print(logo)
print(f'You have {points} points.')
while True:
    print('\n'*5)

    print('Guess who has more instagram followers: ')
    p1 = choice(org_data_name)
    p2 = choice(org_data_name)
    ind1 = org_data_name.index(p1)
    ind2 = org_data_name.index(p2)

    print(f'1. {p1} has {org_data_followers[ind1]} followers.')
    print(f'2. {p2}  has ___ followers')
    user_choice = int(input(f'Enter 1 for {p1} or 2 for {p2}. \n'))
    if ind1 < ind2 and user_choice == 1:
        print(f'Awesome! Current points {points+1}')
        print(f'1. {p1} has {org_data_followers[ind1]}')
        print(f'2. {p2}  has {org_data_followers[ind2]} followers')
        points += 1

    elif ind1 > ind2 and user_choice == 2:
        print(f'Awesome! Current points {points + 1}')
        print(f'1. {p1} has {org_data_followers[ind1]}')
        print(f'2. {p2}  has {org_data_followers[ind2]} followers')
        points += 1

    else:
        print('Hard Luck')
        print(f'1. {p1} has {org_data_followers[ind1]}')
        print(f'2. {p2}  has {org_data_followers[ind2]} followers')
        print(f'You finished with {points} points.')
        print('\n'*2)
        play_again = input('Enter y to play again or enter n to quit.\n')
        if play_again.lower() == 'y':
            points = 0
            continue
        else:
            break

