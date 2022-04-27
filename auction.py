from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print('Welcome to the auction')
auc = {}
while True:
    name = input('Enter your name. ')
    amt = int(input('Enter your amount for the bid.$'))
    auc[name] = amt
    choice = input('Are there anymore bidders? Enter y or n ')
    if choice.lower() == 'y':
        clear()
        continue
    else:
        break

maximum = 0
auc_name = ''
for items in auc:
    if auc[items] > maximum:
        maximum = auc[items]
        auc_name = items

print(f'The winner of auction is {auc_name} with the highest bid ${maximum} .')


