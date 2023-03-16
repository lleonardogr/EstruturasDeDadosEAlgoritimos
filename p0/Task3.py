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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
list_of_codes = []
for call in calls:
    incoming_call = call[0]
    if "(080)" in incoming_call:
        number_called_code = None
        if "(" in call[1]:
            # prefix_range = 0
            # for letter in number_called:
            #     if letter!=")":
            #         prefix_range += 1
            #     else:
            #         break
            # number_called_code = number_called[0:prefix_range+1]
            number_called_code = call[1].split(')')[0] + ')'
        elif " " in call[1] and call[1][0] in ['7','8','9']:
            number_called_code = call[1][0:4]
        if number_called_code not in list_of_codes:
                list_of_codes.append(number_called_code)

list_of_codes.sort()
for code in list_of_codes:
    print(code)

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
bangalore_calls = 0
number_local_calls = 0
for call in calls:
    incoming_call, number_called = call[0],call[1]
    if incoming_call[0:5] == "(080)":
        bangalore_calls += 1
        if number_called[0:5] == "(080)":
            number_local_calls += 1



print(str(round(number_local_calls/bangalore_calls* 100,2)) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
