#!/usr/bin/python3
import sys
import csv

def addHeaders(arr):
    header = ["Date", "Time", "aet", "BC Conc", "Flow", "Zero Signal", "Sensing Signal", "Ref Zero", "Ref Sens", "Bypass Fraction", "Tape Attenuation"]

    arr = [header] + arr

    return arr

def formatDate(date):

    # Delimiter
    slash = '/'

    # Split string using slice notation
    year = date[0:4]
    month = date[4:6]
    day = date[6:]

    # Combine split strings with delimiter(s)
    new_date = year + slash + month + slash + day

    return new_date

def formatTime(time):

    # Delimiter
    colon = ':'

    # Edge-Case for 12:00 AM (keep leading zeros)
    if time[0] == "0" and time[1] == "0":
        hour = time[0:2]
        minutes = time[2:]
        new_time = hour + colon + minutes
        return new_time

    # Strip leading zero from time (if between 1:00 AM - 12:00 PM)
    elif time[0] == "0":
        time = time.lstrip("0")
        hour = time[0:1]
        minutes = time[1:]
        new_time = hour + colon + minutes
        return new_time

    # Any other time is dealt with here (12:00 PM - 12:00 AM)
    hour = time[0:2]
    minutes = time[2:]
    new_time = hour + colon + minutes
    return new_time

# Function to write new list to CSV
def writeFile(arr, file):
    outputName = file[:2]
    with open(outputName + '_aet.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(arr)

# Function to read CSV File
def readFile(filename):
    # Open File
    file = open('%s' % filename, 'r')

    # Use csv_reader to parse file
    csv_reader = csv.reader(file, delimiter=",")

    csv_contents = []

    # Read CSV into list
    for row in csv_reader:
        csv_contents.append(row)

    # Remove empty rows from array (due to .txt file formatting)
    csv_contents = [row for row in csv_contents if len(row) > 0]    # row added if condition true

    # Remove rows that contain no data after 'aet' column
    #csv_contents = [row for row in csv_contents if row[3] != ""]    # row added if condition true

    file.close()
    return csv_contents

# Function iterates through first and second elements of every row and converts to a readable date/time
def modifyElements(arr):
    for i in range(0, len(arr)):
        arr[i][0] = formatDate(arr[i][0])   # modifies every 1st column value
        arr[i][1] = formatTime(arr[i][1])   # modifies every 2nd column value

    return arr

def main():
    file = sys.argv[1] # get filename from CLI
    csv = readFile(file) # read file into 2D array (headers not included)
    csv = modifyElements(csv) # date/time conversion
    if (file[:2] !=  'FV'):
        csv = addHeaders(csv) # insert headers
    writeFile(csv, file) # output result
    return


# Self-Execute main()
if __name__ == "__main__":
    main()
