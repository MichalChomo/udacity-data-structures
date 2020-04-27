"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def maybe_update_max_duration_and_number(number, number_duration, current_max_duration,
                                         current_number_with_max_duration):
    if number_duration > current_max_duration:
        return number, number_duration
    else:
        return current_number_with_max_duration, current_max_duration


number_to_duration = {}
max_duration = 0
number_with_max_duration = ''

for line in calls:
    calling_number = line[0]
    receiving_number = line[1]
    duration = int(line[3])
    for num in [calling_number, receiving_number]:
        number_to_duration[num] = number_to_duration.get(num, 0) + duration
        number_with_max_duration, max_duration = maybe_update_max_duration_and_number(num,
                                                                                      number_to_duration[num],
                                                                                      max_duration,
                                                                                      number_with_max_duration)

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(number_with_max_duration,
                                                                                          max_duration))
