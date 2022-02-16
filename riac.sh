#!/bin/bash

#----------------------------------------------------------------------------
# Executes file (respective to AET || EPC)
function execute_file () {
	if [[ "$1" == *"epc"* ]]
		then
			echo "EPC TRIGGERED"
			command ./epc_format.py "$1"
	elif [[ "$1" == *"FV_aet.csv"* ]]
		then
			echo "FV_AETH TRIGGERED"
			command ./FV_AETH.py "$1"
	else
		echo "AET TRIGGERED"
		command ./aet_format.py "$1"
	fi } # <--- DON'T MOVE THIS BRACKET (functional formatting)

#----------------------------------------------------------------------------

# Error Handling (if program is executed with arguments)
if [[ $# != 0 ]]
	then
		echo "Do not run with arguments.."

#----------------------------------------------------------------------------
else

	echo Looking for files with extension .txt/.csv in folder

	# create array and count (length of array)
	files=()
	count=0

	# assess every file in given directory
	for fname in *
	do
		# add desired files to array
		if [[ $fname == *.txt ]] || [[ $fname == *.csv ]]
			then
				files+=( "$fname" )
				((count++))
		fi
	done

	# no files found
	if [[ $count == 0 ]]
		then
			echo No file found.

	# one file found
	elif [[ $count == 1 ]]
		then
			echo 1 file found:
			echo $'\t'"${files[0]}"
			execute_file "${files[0]}"

	# multiple files found
	else

		echo "$count" files found:

		# print all files in array
		for fname in "${files[@]}"
		do
			echo $'\t'"$fname"
			execute_file "$fname"
		done
	fi
fi
#----------------------------------------------------------------------------
