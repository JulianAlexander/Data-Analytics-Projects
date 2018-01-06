import csv
import os


with open(r"C:\Users\thela\OneDrive\UCB Data Bootcamp\Homework #3\paragraph.csv",newline='') as csvfile:
    
    f = csvfile.read()
    csvreader = csv.reader(csvfile, delimiter=' ')
    word_list = []
    new_list = []
    num_sentences = (f.count('.')+ f.count('?')+f.count('!')) # Number of sentences. Counts the number of periods, question marks, exclamation marks in the file
    num_words = (f.count(' ')+2) #Number of Words. Function counts the number of spaces and adds 2 to account for the first and last words of the file.
    for items in f:
        if items != " ":
            new_list.append(items) #This rejects all of the spaces in the string, and adds the letters to a new list, which we can then take the length of to give us the number of characters minus spaces
    
    print("Paragraph Analysis:")
    print("------------------------------------------")
    print("Approximate Word Count: " + str(num_words))
    print("Approximate Sentence Count: " + str(num_sentences))
    print("Approximate Number of Characters (including spaces): " + str(len(f))) #prints the total number of characters with spaces
    print("Approximate Number of Characters (minus spaces): " + str(len(new_list)))
    print("Average Letter Count: " + str(len(new_list)/num_words))
    print("Average Sentence Length: " + str(num_words/num_sentences))