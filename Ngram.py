#######################################################################
##
## CS 101
## Program #7
## Name: Harrison Lara
## Email: hrlwwd@mail.umkc.edu
##
## PROBLEM :
## You’ll have 2 files to work with; all_words.csv and total_counts.csv.  All words will contain all the words that
## the user can compare with their counts in literature for each year.  total _counts has the counts of all words by
## year, so that we can find the relative frequency.
##
##
## ALGORITHM :
##
##  •	Need to find the relative frequency and word commonality
##  •	Use functions
##  •	Classes/ objected oriented programming not needed
##  •	Ask user if they want to use ngram viewer or quit
##      o	1 or 2
##      o	Try and except
##  •	For all_words.csv
##      o	Each line is how often the word is used and how many books it came out of
##      o	Last value does not matter (skip)
##  •	For total_count.csv
##      o	Each line is the year and how many times a word occurred in the literature
##  •	Relative frequency formula
##      o	Amount of times word used in a year/the total words in the year
##      o	Times by 100 after
##  •	Get user input
##      o	Ask for what word needs to be searched for
##          	What word do you want to get the frequencies from:
##      o	Ask for starting year
##          	Must be between 1505 and 2008
##          	Must be an integer
##  •	Int(input
##          	Must have range from only the start year to 2008 (ex. User inputs 1900 so it must be from 1900 – 2008
##              or from start-end date)
##          	Try and except
##      o	Ask for ending year
##          	Must be between 1505 and 2008
##          	Must be an integer
##  •	Int(input
##          	(ex. User inputs 1900 so it must be from 1900 – 2008, or from start- end date)
##  •	Try and except
##  •	Display results in a table
##  •	Use Ngram Viewer
##      o	Table to show output of data to user
##      o	Three columns
##          	Year
##          	Word1 with frequencies
##           	Word2 with frequencies
##  •	Import csv module
##  •	Open file
##      o	File=open(‘all_words.csv’)
##      o	Csv_file = csv.reader(file)
##  •	Get list of strings for each line
##      o	For line in csv_file:
##      o	Print(line)
##      o	File.close()
##          	Possible functions to use from prior programs (maybe)
##      o	Relative frequency and word commonality
##
## ERROR HANDLING:
##      Value Error, date must be higher than the start date or 1505
##
## OTHER COMMENTS:
##     None.
##
########################################################################

# Imports
import csv

#Functions
def input_word(validate):
    ''' User input of word'''
    while True:
        word = input("Enter a word to get the frequencies of ==> ")    
        
        if word in validate:
            return word
        else:
            print (word , "was not found, please input a new word")


def start_year():
    ''' User input the start year'''
    while True:
        try:
            year1 = input("Enter a start date ==> ")
            if year1 == "":
                year1 = 1900
            if int(year1) >= 1505 and int(year1) <= 2008:
                return int(year1)
            else:
                print("Please enter a date between 1505 and 2008")
        except ValueError:
            print("You must enter a date")

        
def end_year(year1):
    ''' User input the end year'''
    while True:
        try:
            year2 = input("Enter the end date ==> ")
            if year2 == "":
                year2 = 2008
            if int(year2) >= int(year1) and int(year2) <= 2008:
                return int(year2)
            else:
                print("You must enter a date between", year1," and 2008")
        except ValueError:
            print("You must enter a date")

def get_word(file):
    '''Find word for dictionary'''
    validate = {}
    for line in file:
        word = line[0]
        date = int(line[1])
        count = int(line[2])
        if word in validate:
            validate[word].append([date , count])
        else:
            validate[word] = [[date,count]]
    return validate


def get_count(file):
    ''' Find how often the word appears'''
    counter = {}
    for line in file:
        counter[int(line[0])] = int(line[1])
    return counter


def frequency(word, validate, counter):
    '''Find the frequency of the words'''
    freq = {}
    for total_year in validate[word]:
        freq[total_year[0]] = (total_year[1]/counter[total_year[0]])*100
    return freq


def table_format(year1, year2 ,one_word, two_word, one_freq, two_freq):
    '''Create how the table should appear to the user'''
    print("{:^}".format("Ngram Table \n"))
    print("{:^8s}{:^12s}{:^12s}".format("Year", one_word, two_word))
    print("=" * 30)
    for date in range (year1, year2 + 1):
        freq1 = one_freq[date] if date in one_freq else 0
        freq2 = two_freq[date] if date in two_freq else 0
        print("{:^10d}{:^10.6f}{:^10.6f}".format(date,freq1,freq2))
    print("")

    
def print_table():
    ''' Print out the results on the table for the user'''
    total_count = csv.reader(open("total_counts.csv"))
    all_words = csv.reader(open("all_words.csv"))
    all_words = get_word(all_words)
    total_count = get_count(total_count)
    word_one = input_word(all_words)
    word_two = input_word(all_words)
    year1 = start_year()
    year2 = end_year(year1)
    one_freq = frequency(word_one, all_words, total_count)
    two_freq = frequency(word_two, all_words, total_count)
    table_format(year1, year2 ,word_one, word_two, one_freq, two_freq)


def main():
   '''combines the final steps to run the entire program as one'''
user = "y"

while user != "q":
    print("Ngram Viewer \n")
    print("1. Ngram Table")
    print("Q. Quit")
    print("")
    user = input("==> ").lower()
    if user == "1":
        print_table()
    elif user != "q":
        print("Please choose a valid option from either '1' or 'Q' \n")
# Main
main() # Main program running all functions as a whole
