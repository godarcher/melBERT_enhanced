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
data_path = "C:\\Users\\joost\\Documents\\work\\radboud\\dataset_txt_meta"

#*###############
#?ACTUAL PROGRAM#
#*###############

#counters
parsed_files = 0
total_covid_score = 0

#For all files in data path
for filename in os.listdir(data_path):

    #If filename contains .txt and does not contain the word meta (for seperating metadata) nor sentences (for general metadata and collecitons)
    if filename.endswith(".txt") and filename.find("meta") == -1 and filename.find("sentences") == -1:
        #open file and read contents to string
        file_path = data_path + "\\" + filename
        file_path_meta = file_path.replace(".txt","") + "_meta.txt"
        covid_path = data_path + "\\" + "covid_scores.txt"
        #initiate score (and reset)
        covid_score = 0

        #open the file with read permission
        with open(file_path, 'r') as file:
            #We replace the newlines and make it lowercase
            data = file.read().replace('\n', '').lower()
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

            with open(file_path_meta, 'r') as filem:
                #We replace the newlines and make the data lowercase for case insensitivy
                metadata = filem.read().replace('\n','').lower()
                words_index = metadata.find("Length:") + 8 #+8 for length of "Length: "
                words_end_index = metadata.find("words") -1 #this won't deliver problems because length is early in metadata
                words = int(metadata[words_index:words_index]) #cast to int to be able to do math with it

                #? We divide the covid score by the amount of words in the text to make the score word sensitive
                covid_score = covid_score / words

                #we close so we can open as append
                filem.close
            
            #? We append the calculated data to one big covid_scores file
            with open(covid_path, 'w') as filecov:
                filecov.write("Filename: " + str(filename) + "Covid score: " + str(covid_score) + "\n")

            #* Update counters
            total_covid_score = total_covid_score + covid_score
            parsed_files = parsed_files + 1


            

            #TODO
            #*1: open covid meta file 
            #*2: get amount of words and divide score by that
            #*4: Add coronascore to metadata file
            #5: save amount of files parsed, save total covid score of all files
            #6: divide total covid score by amount of files parsed
            #7: adjust the medium score (by adding/removing a bit to get low and high score)
            #8: scrape amount of txt files lower then and higher then score
            #9: if content with 8 save subsets of dataset accordingly


    else:
        continue
