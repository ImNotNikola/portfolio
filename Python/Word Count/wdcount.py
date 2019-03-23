# Nikola Kuhar
#9/3/2015

#Imports sys library into the program to access argv
import sys

#Takes in file name to open from command line, assigns to variable "file"
file = sys.argv[1]

#Opens file gotten above and stores it to variable text
text = open(file)
#create dictionary as required
wdcount = {}
#Create variable to keep total count
count = 0

#For loop to run through all words in file
for word in text.read().split():
        #Increment count for each word
        count += 1
        #Checking for new word, if new sets value to 1; if not increments word counter
        if word not in wdcount:
                #Sets value[word] to 1
                wdcount[word] = 1
        else:
                #Increments word because the word already exists
                wdcount[word] += 1

print "The total word count for the file %s is: "% str(sys.argv[1]), count #prints total word count
print "The unique word count for the file %s is: "% str(sys.argv[1]), len(wdcount.items()) #Prints number of unique words
print "The following words are in descending order for the file %s: "% str(sys.argv[1])
#For loop iterates through wdcount and sorts them by descending order
for k,v in sorted(wdcount.items()):
        #Checks if the length of the word is greater or equal to 4
        if len(k) >= 4:
           print k, v #Prints word and count based on sort