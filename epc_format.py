#!/usr/bin/python3
import sys
import csv

def addHeaders(arr):
    header = ["Date", "Time", "Errors", "PM0.1 Conc", "Sample Time", "Live Time", "Particle Count", "Photodetector", "Res", "Pulse Height", "PHStdDev"]

    arr = [header] + arr

    return arr

# Function to write new list to CSV
def writeFile(arr, file):
    outputName = file[:2]
    with open(outputName + '_epc.csv', 'w') as f:
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

    # Removes empty rows from array (due to .txt file formatting)
    csv_contents = [row for row in csv_contents if len(row) > 0]

    file.close()
    return csv_contents

def main():
    file = sys.argv[1] # get filename from CLI
    csv = readFile(file) # read file into 2D array (headers not included)
    csv = addHeaders(csv) # insert headers
    writeFile(csv, file) # output result
    return

# Self-Execute main()
if __name__ == "__main__":
    main()
