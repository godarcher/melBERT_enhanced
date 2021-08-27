"""
The following program is an attempt with limited time and resources, to classify batches of txt files
we try to sort the files by giving them a score based upon the likelihood of being a covid text
The program was written by Joost Grunwald for the Radboud University and is made for dutch text

CORONAWOORDEN DUBBEL
corona covid ncov

CORONAWOORDEN ENKEL
virus quarantaine viroloog
RIVM vaccin astrazeneca
pfizer moderna biontech
prik epidemie pandemie
quarantaine isolatie lockdown
intensive care immuniteit 1.5 meter
1,5 meter besmettingen

IDEA BEHIND THE ALGORITHM
coronaword in title --> 6 punten
coronaword in bylight --> 3 punten
coronaword --> 1 punt
corona words in first 5 setences --> dubble point
dubble corona words --> dubble points
"""

#*################
#?IMPORT SETTINGS#
#*################
import os
from pathlib import Path

#*#########
#?SETTINGS#
#*#########
data_path = "C:\Users\Josso\Desktop\.txt incl. meta\dataset_txt_renamed"

#*###############
#?ACTUAL PROGRAM#
#*###############
#For all files in data path
for filename in os.listdir(data_path):

    #If filename contains .txt and does not contain the word meta (for seperating metadata)
    if filename.endswith(".txt") and filename.find("meta") == -1:
        #open file and read contents to string
        file_path = data_path + "\\" + filename
        #initiate score (and reset)
        covid_score = 0

        #open the file with read permission
        with open(file_path, 'r') as file:
            #We replace the newlines
            data = file.read().replace('\n', '')
            #make data lowercase for non uppercase sensitive searching
            data = data.lower()
            #Covid word lists
            double_cov_words = ["corona", "covid", "ncov"]

            single_cov_words = ["virus", "quarantaine", "viroloog", "rivm", "vaccin", "astrazeneca",
                                "pfizer", "moderna", "biontech", "prik", "epidemie", "pandemie",
                                "quarantaine", "lockdown", "intensive care", "immuniteit", "1.5 meter", "isolatie",
                                "1,5 meter", "besmettingen"]

            #actual counting of covid words, for each word in double_cov list
            for double_word in double_cov_words:
                #we count the occurences in the text file
                count = data.count(double_word)
                #If there is at least one occurence
                if count != 0:
                    #we add to the score
                    count = count * 2
                    covid_score += count 

            #actual counting of covid words, for each word in single_cov list
            for single_word in single_cov_words:
                #we count the occurences in the text file
                count = data.count(single_word)
                #If there is at least one occurence
                if count != 0:
                    #we add to the score
                    covid_score += count 


    else:
        continue