Alg. 7
•	Need to find the relative frequency and word commonality
•	Use functions
•	Classes/ objected oriented programming not needed
•	Ask user if they want to use ngram viewer or quit
o	1 or 2
o	Try and except
•	For all_words.csv
o	Each line is how often the word is used and how many books it came out of
o	Last value does not matter (skip)
•	For total_count.csv
o	Each line is the year and how many times a word occurred in the literature
•	Relative frequency formula
o	Amount of times word used in a year/the total words in the year
o	Times by 100 after
•	Get user input
o	Ask for what word needs to be searched for 
	What word do you want to get the frequencies from:
o	Ask for starting year
	Must be between 1505 and 2008
	Must be an integer
•	Int(input
	Must have range from only the start year to 2008 (ex. User inputs 1900 so it must be from 1900 – 2008 or from start-end date)
	Try and except
o	Ask for ending year
	Must be between 1505 and 2008
	Must be an integer
•	Int(input
	(ex. User inputs 1900 so it must be from 1900 – 2008, or from start- end date)
•	Try and except
•	Display results in a table
•	Use Ngram Viewer
o	Table to show output of data to user
o	Three columns
	Year
	Word1 with frequencies
	Word2 with frequencies
•	Import csv module
•	Open file
o	File=open(‘all_words.csv’)
o	Csv_file = csv.reader(file)
•	Get list of strings for each line
o	For line in csv_file:
o	Print(line)
o	File.close()
	Possible functions to use from prior programs (maybe)
o	Relative frequency and word commonality




