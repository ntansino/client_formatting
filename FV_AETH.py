#!/usr/bin/python3
import sys
import pandas as pd
import datetime

def main():
    file = sys.argv[1] # get filename from CLI
    today = datetime.date.today() # get today's date (for file naming)

    print("filename = %s" % file) #debugging

    df = pd.read_csv(file, sep=",") # read file into CSV dataframe

    # adding column headers
    df.columns = ["Date", "Time", "aet", "UVPM", "ex", "ex", "ex", "ex", "BC Conc", "ex", "Flow"]

    df.drop(["UVPM", "ex"], axis=1, inplace=True) # delete unneeded columns


    print(df) #debugging

    df.to_csv("%s_FV_aet33.csv" % today, index=False) # write file

    print(df) #debugging

    return

# Self-Execute Main
if __name__ == "__main__":
    main()
