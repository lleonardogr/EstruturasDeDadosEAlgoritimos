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
def check_unique_phones(table,unique_phones):
    for column in table:
        if column[0] not in unique_phones:
            unique_phones.append(column[0])
        if column[1] not in unique_phones:
            unique_phones.append(column[1])

unique_phones=[]
check_unique_phones(texts, unique_phones)
check_unique_phones(calls, unique_phones)


print("There are "+str(len(unique_phones))+" different telephone numbers in the records.")
