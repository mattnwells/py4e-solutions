"""
Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

dictionary_hours = dict()                       # Initialize variables
lst = list()

fname = input('Enter file name: ')              # mbox-short.txt
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 5 or words[0] != 'From': 
        continue

    col_pos = words[5].find(':')
    hour = words[5][:col_pos]
    if hour not in dictionary_hours:
            dictionary_hours[hour] = 1       # First entry
    else:
            dictionary_hours[hour] += 1      # Additional counts

for key, val in list(dictionary_hours.items()):
    lst.append((key, val))       # Fills list with hour, count of dictionary

lst.sort()                       # Sorts by hour 

for key, val in lst:
    print(key, val)