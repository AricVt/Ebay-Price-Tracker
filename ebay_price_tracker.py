#!/usr/bin/python3

# Setup modules and variables
import requests
import bs4
import re
import datetime
import sys
import csv

ebay_link ='https://www.ebay.com/sch/i.html?_dcat=177&_fsrp=1&rt=nc&_from=R40&Processor=Intel%2520Core%2520i7%252D8665U%7CIntel%2520Core%2520i7%252D8650U%7CIntel%2520Core%2520i7%25208th%2520Gen%252E&LH_PrefLoc=1&_nkw=Lenovo+thinkpad+T480+i7&_sacat=0&Model=Lenovo%2520ThinkPad%2520T480&Maximum%2520Resolution=1920%2520x%25201080%7C2560%2520x%25201440'

# Get site data from html link and convert using Beautiful Soup
def get_prices(link):
    price_lst = []
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text,"lxml")

# Filter out price data into price_lst
    for item in soup.select('.s-item__price')[1:]:
        if 'to' not in item.text:
            if 'ITALIC' not in str(item):
                price_lst.append(float(re.sub(r'[^\d.]', '', item.text)))
# Average and return the data in the list            
    price_ave = ((sum(price_lst))/len(price_lst))
    
    return(price_ave)

# Append price data to CSV file
def save_file(prices):
    save_data = [datetime.datetime.today().strftime('%b-%d-%Y'), prices]
    
    with open('ebay_prices.csv', 'a', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(save_data)

# Read CSV file and calculate average price
def read_data():
    
    try:
        with open('ebay_prices.csv', encoding='utf-8') as data:
            csv_data = csv.reader(data)
            data_lines = list(csv_data)
            read_prices = []
            for line in data_lines:
                read_prices.append(float(line[1]))
            return [data_lines[-1][0],round(sum(read_prices)/len(read_prices),2)]
    
    except:
        print('Error: Data File Does Not Exist')
        return[0,0]

# Run the code if main program

if __name__ == '__main__':
    scrape = ''
    read_file = ''
    print('EBay Price Tracker')
    print()
    
    # Ask user if they want to retrieve current prices from link
    while True:
        scrape = input('Do you want to get current search prices? ')
        if scrape.lower() in ['y', 'n', 'x']:
            if scrape.lower() == 'x':
                exit()
                
            else:    
                break
        else:
            print ('Please enter y (yes), n (no), or x (exit)')
            
    # Run the search if requested
    if scrape.lower() == 'y':
        print('Getting data...')
        save_file(get_prices(ebay_link))
        
    # Ask the user if they want to read the saved data file
    while True:
        display = input('Do you want to display the average saved price? ')
        if display.lower() in ['y', 'n', 'x']:
            if display.lower() == 'x':
                exit()
                
            else:    
                break
        else:
            print ('Please enter y (yes), n (no), or x (exit)') 
            
    # Display the report if requested
    if display.lower() == 'y':
        file_result = read_data()
        print(f'The average price is ${file_result[1]}, the last data was taken {file_result[0]}')
    
    print('Program Complete')
    exit()
    


