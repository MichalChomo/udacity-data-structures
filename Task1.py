"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

calls_numbers = {num for line in calls for num in line[:2]}
texts_numbers = {num for line in texts for num in line[:2]}

print('There are {} different telephone numbers in the records.'.format(len(calls_numbers | texts_numbers)))
