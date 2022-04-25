import random
from main import stages, logo
from newmain import word_list
print(logo)
print("Welcome to Hangman")
lives = 7
print(f'You have {lives} lives.')

# randomly a word is selected
word = random.choice(word_list)
new_list = []
for i in range(len(word)):
    new_list.append('_')
# generate as many dashes as there are in word
dash = ""
for i in range(len(word)):
    dash += '_'
'''
we are storing in the form of a list because mutation is not allowed in list; i.e if 
str is a sting containing dashes then str[count] = 'a' is not permissible. 
'''
print(f'Guess the word {dash}')
# Take input from user
life = 6


while True:
    count = 0
    print(new_list)
    flag = 0
    user_input = input('Enter a letter: ')
    letter = user_input[count]

# Check the input is correct or not
    for i in word:
        if user_input == i:
            new_list[count] = i
            flag = 1
        count += 1

# Check if game is finished
    if '_' not in new_list:
        print("You win!")
        print(new_list)
        break
# Letter is incorrect
    if flag == 0:
        print(stages[life])
        life -= 1
# Player has no lives left
    if life < 0:
        print('Game over')
        print(f'The word was {word}')
        break

