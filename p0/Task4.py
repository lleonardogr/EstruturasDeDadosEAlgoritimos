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
marketing_numbers,outgoing_calls = [],[]
for call in calls:
    outgoing_calls.append(call[1])
for text in texts:
    outgoing_calls.append(text[1])

for call in calls:
    if call[0] not in outgoing_calls:
        marketing_numbers.append(call[0])
for text in texts:
    if text[0] not in outgoing_calls:
        marketing_numbers.append(text[0])


marketing_numbers.sort()
for marketing_number in list(dict.fromkeys(marketing_numbers)):
    print(marketing_number)


    
    

