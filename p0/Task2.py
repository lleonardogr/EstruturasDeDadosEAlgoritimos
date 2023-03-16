"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

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
calls_by_time = {}
for call in calls:
    # Collect the durations for calling phone numbers (`call[0]`)
    if call[0] not in calls_by_time: 
        calls_by_time[call[0]] = int(call[3])
    else:
        calls_by_time[call[0]] += int(call[3])
    # Collect the durations for receiving phone numbers (`call[1]`)
    if call[1] not in calls_by_time: 
        calls_by_time[call[1]] = int(call[3])
    else:
        calls_by_time[call[1]] += int(call[3])

message = str.format("{longest_call} spent the longest time, {total_time} seconds, on the phone during September 2016.",
                         longest_call=max(calls_by_time, key=calls_by_time.get), total_time=max(calls_by_time.values()))
print(message)
        
