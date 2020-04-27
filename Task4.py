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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

calling_numbers = set()
receiving_call_numbers = set()
texting_numbers = {num for line in texts for num in line[:2]}

for line in calls:
    calling_numbers.add(line[0])
    receiving_call_numbers.add(line[1])

print('These numbers could be telemarketers:')
print('\n'.join(sorted(calling_numbers - texting_numbers - receiving_call_numbers)))
