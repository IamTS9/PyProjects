# import modules for web scraping
import requests
import bs4
result = requests.get('https://www.x-rates.com/table/?from=INR&amount=1')
soup = bs4.BeautifulSoup(result.text, 'lxml')

# scrape the required data
name = soup.select('.moduleContent')
scraped_data = name[0].text

# list to remove unwanted data which is also scraped
list_scraped_data = list(scraped_data.split('\n'))
# removing unwanted data which is also scraped
del list_scraped_data[0:14]
del list_scraped_data[55:65]
# to remove '' in the list
for num in range(136):
    list_scraped_data.remove('')

# empty dictionaries
INR_to_other = {}
other_to_INR = {}
# adding values to empty dictionary
for item in list_scraped_data:
    INR_to_other[list_scraped_data[0]] = list_scraped_data[1]
    other_to_INR[list_scraped_data[0]] = list_scraped_data[2]
    del list_scraped_data[0:3]

ask = ''
while ask not in ['1', '2', '3']:
    ask = (input
           ('If you want convert INR to some currency enter 1 , enter 2 for converting given currency into INR'
            ' or enter 3 for converting any other currencies  \n'))
int_ask = int(ask)
if int_ask == 1:
    print('Converter to convert INR to the currencies given below. \n')
    print('Please select any one of the currency given below.\n')
    for item in INR_to_other.keys():
        print(item)
    print('Please copy the correct name of the currency. \n')
    try:
        ask_2 = input('Enter the name of the currency you want to convert INR into: \n')
        INR_amt = int(input('Please enter the amount in INR: \n'))
        print('\n'*2)
        value_ask_2 = INR_to_other[ask_2]
        final_value = INR_amt*float(value_ask_2)
        print(f'{INR_amt} INR is equivalent to {final_value} {ask_2}'+'s')
    except KeyError:
        print('Please enter the exact name of currency. ')
    except ValueError:
        print('Please enter amount correctly. ')
elif int_ask == 2:
    print('Converter to convert given currency to INR. \n')
    print('Please select any one of the currency given below.\n')
    for item in INR_to_other.keys():
        print(item)
    print('Please copy the correct name of the currency. \n')
    try:
        ask_2 = input('Enter the name of the currency : \n')
        amt = int(input(f'Please enter the amount in {ask_2}: \n'))
        print('\n'*2)
        value_ask_2 = other_to_INR[ask_2]
        final_value = amt*float(value_ask_2)
        print(f'{amt} {ask_2}s is equivalent to {final_value} INR. \n')
    except KeyError:
        print('Please enter the exact name of currency. ')
    except ValueError:
        print('Please enter amount correctly. ')
elif int_ask == 3:
    print("Converter to convert two currencies of given choice \n ")
    print('Please select any one of the currency given below.\n')
    for item in INR_to_other.keys():
        print(item)
    print('Please copy the correct name of the currency. \n')
    try:
        ask_curr_1 = input('Enter the name of first the currency : \n')
        ask_curr_amt = int(input('Enter the amount you want to convert: \n'))
        ask_curr_2 =  input('Enter the name of currency you want to convert to: \n')
        curr_1_final = other_to_INR[ask_curr_1]
        temp_amt_1 = ask_curr_amt*float(curr_1_final)
        curr_2_final = other_to_INR[ask_curr_2]
        temp_amt_2 = ask_curr_amt * float(curr_2_final)
        fin_amt = temp_amt_1/temp_amt_2
        print(f'{ask_curr_amt} in {ask_curr_1}s is equivalent to {fin_amt} in {ask_curr_2}s ')
    except KeyError:
        print('Please enter the exact name of currency. ')
    except ValueError:
        print('Please enter amount correctly. ')
print('Thanks for using currency converter')



