# Ebay-Price-Tracker

This is a program created as a capstone project for the Udemy class 
[The Complete Python Bootcamp From Zero to Hero in Python](https://www.udemy.com/course/complete-python-bootcamp/)

This is my first project written from scratch using the knowledge from the above course. 

This program loads an [Ebay search address](https://www.ebay.com/sch/i.html?_dcat=177&_fsrp=1&rt=nc&_from=R40&Processor=Intel%2520Core%2520i7%252D8665U%7CIntel%2520Core%2520i7%252D8650U%7CIntel%2520Core%2520i7%25208th%2520Gen%252E&LH_PrefLoc=1&_nkw=Lenovo+thinkpad+T480+i7&_sacat=0&Model=Lenovo%2520ThinkPad%2520T480&Maximum%2520Resolution=1920%2520x%25201080%7C2560%2520x%25201440)

This page is loaded using requests and then pulls data using beautifulsoup4. The price data is then averaged and saved in a CSV file with a date stamp. The program can then read this file, averaging all past data loaded into the file and reports an average so the price can be tracked over time.


