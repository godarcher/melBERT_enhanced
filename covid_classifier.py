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

# counters
parsed_files = 0
total_covid_score = 0
covid_scores = []
not_enough_words = 0
total_words = 0

# reset covid file once
covid_path = data_path + "\\" + "covid_scores.txt"
with open(covid_path, 'w') as filecovr:
    filecovr.close()

# For all files in data path
for filename in os.listdir(data_path):

    # If filename contains .txt and does not contain the word meta (for seperating metadata) nor sentences (for general metadata and collecitons)
    if filename.endswith(".txt") and filename.find("meta") == -1 and filename.find("sentences") == -1 and filename.find("covid_scores") == -1:
        # open file and read contents to string
        file_path = data_path + "\\" + filename
        file_path_meta = file_path.replace(".txt", "") + "_meta.txt"
        covid_path = data_path + "\\" + "covid_scores.txt"
        # initiate score (and reset)
        covid_score = 0
        # This bool is used to determine wether or not to save a file
        use_file = True

        words = 0

        # open the file with read permission
        with open(file_path, 'r', encoding='utf-8') as file:
            # We replace the newlines and make it lowercase
            data = file.read().replace('\n', '').lower()
            # Covid word lists
            double_cov_words = ["covid-19", "ncov", "biontech", "astrazeneca", "moderna"
                                "pfizer", "immuniteit", "intensive care"]

            single_cov_words = ["quarantaine", "viroloog", "vaccin", "reproductiefactor", "rivm"
                                " prik ", "epidemi", "ic-patiënten", "ic-opname", "Sars", "ic-arts"
                                "1.5 meter", "isolatie", "besmettingsgraad", "beademing", "sterfgevallen"
                                "1,5 meter", "besmettingen", "ic-patiënten", " ic ", "wuhan", "sterftegevallen"]

            half_cov_words = ["corona", "virus", "covid", "getest", "testen"
                              "pandemie", "lockdown", "maatregelen", "ziekenhuis", "longen"]

            neg_cov_words = ["voetbal", "darten", " WK "]

            # actual counting of covid words, for each word in double_cov list
            for double_word in double_cov_words:
                # we count the occurences in the text file
                count = data.count(double_word)
                # If there is at least one occurence
                if count != 0:
                    # we add to the score
                    count = count * 1.8
                    covid_score += count

            # actual counting of covid words, for each word in single_cov list
            for single_word in single_cov_words:
                # we count the occurences in the text file
                count = data.count(single_word)
                # If there is at least one occurence
                if count != 0:
                    # we add to the score
                    covid_score += count

            for single_word in half_cov_words:
                # we count the occurences in the text file
                count = data.count(single_word)
                # If there is at least one occurence
                if count != 0:
                    # we add to the score
                    covid_score += (0.35 * count)

            for single_word in neg_cov_words:
                # we count the occurences in the text file
                count = data.count(single_word)
                # If there is at least one occurence
                if count != 0:
                    # we add to the score
                    covid_score -= (0.35 * count)

            # remove duplicates caused by combination of corona and virus which both are keywords
            coronavirus = data.count("coronavirus")
            # If there is at least one occurence
            if coronavirus != 0:
                # remove form the score
                covid_score -= 0.35 * coronavirus

            # remove duplicates caused by combination of covid and covid-19 which both are keywords
            coronavirus = data.count("covid-19")
            # If there is at least one occurence
            if coronavirus != 0:
                # remove form the score
                covid_score -= 0.35 * coronavirus

            # Make sure texts don't go below zero
            if covid_score < 0:
                covid_score = 0

            # Finally we close the file
            file.close()

        with open(file_path_meta, 'r', encoding='utf-8') as filem:
            # We replace the newlines and make the data lowercase for case insensitivy
            metadata = filem.read().replace('\n', '').lower()
            # +8 for length of "Length: "
            words_index = metadata.find("length:") + 8
            # this won't deliver problems because length is early in metadata
            words_end_index = metadata.find("words") - 1
            # cast to int to be able to do math with it
            words = int(metadata[words_index:words_end_index])
            # DEBUG
            if words == 0:
                print(words_index)
                print(words_end_index)
                print(metadata)
                print(filem)
                print(metadata[words_index:words_end_index])

            # * Remove texts with small amount of words (<= 50)
            if words <= 85:
                not_enough_words = not_enough_words + 1
                use_file = False

            # ? We divide the covid score by the amount of words in the text to make the score word sensitive
            covid_score = covid_score * 100 / words

            # we close so we can open as append
            filem.close()

        # ? We append the calculated data to one big covid_scores file
        if use_file == True:
            with open(covid_path, 'a') as filecov:
                filecov.write("Filename: " + str(filename) +
                              " Covid score: " + str(covid_score) + "\n")
                filecov.close()

                # ? Add to the covid scores list
                covid_scores.append(covid_score)

                # * Update counters
                total_covid_score = total_covid_score + covid_score
                total_words = total_words + words
                parsed_files = parsed_files + 1

    else:
        continue

# ? After all files are parsed we calculate a medium score
medium_covid_score = total_covid_score / parsed_files

bottom_covid_score = medium_covid_score * 0.25
half_covid_score = medium_covid_score * 0.5
low_covid_score = medium_covid_score * 0.75
high_covid_score = medium_covid_score * 1.5
two_covid_score = medium_covid_score * 2
top_covid_score = medium_covid_score * 4

# ?counters
bottom_scores = 0
half_scores = 0
low_scores = 0
high_scores = 0
two_scores = 0
top_scores = 0

# * Assignment of scores per percentage
for score in covid_scores:
    # * LOW SCORES
    if score <= bottom_covid_score:
        bottom_scores = bottom_scores + 1
        half_scores = half_scores + 1
        low_scores = low_scores + 1
    elif score <= half_covid_score:
        half_scores = half_scores + 1
        low_scores = low_scores + 1
    elif score <= low_covid_score:
        low_scores = low_scores + 1

    # * HIGH SCORES
    elif score >= top_covid_score:
        top_scores = top_scores + 1
        two_scores = two_scores + 1
        high_scores = high_scores + 1
    elif score >= two_covid_score:
        two_scores = two_scores + 1
        high_scores = high_scores + 1
    elif score >= high_covid_score:
        high_scores = high_scores + 1


# ? Calculate percentage size of subparts of database
bottom_scores_per = bottom_scores/parsed_files * 100
half_scores_per = half_scores/parsed_files * 100
low_scores_per = low_scores/parsed_files * 100
high_scores_per = high_scores/parsed_files * 100
two_scores_per = two_scores/parsed_files * 100
top_scores_per = top_scores/parsed_files * 100

# * Output section
print("Files Processed: " + str(parsed_files + not_enough_words))
print("Files Found Useful: " + str(parsed_files))
print("Files Discarded: " + str(not_enough_words))
print("Total Words: " + str(total_words))
print("")
print("Cumulative covid score: " + str(total_covid_score))
print("Bottom covid score: " + str(bottom_covid_score))
print("Half covid score: " + str(half_covid_score))
print("Low covid score: " + str(low_covid_score))
print("High covid score: " + str(high_covid_score))
print("Double covid score: " + str(two_covid_score))
print("Top covid score: " + str(top_covid_score))
print("")
print("Percentage of below bottom scores: " + str(bottom_scores_per))
print("Percentage of below half scores: " + str(half_scores_per))
print("Percentage of below low scores: " + str(low_scores_per))
print("Percentage of above high scores: " + str(high_scores_per))
print("Percentage of above double scores: " + str(two_scores_per))
print("Percentage of above top scores: " + str(top_scores_per))

# ? Save to file section
with open(covid_path, 'a') as filecov:
    filecov.write("Files Processed: " + str(parsed_files + not_enough_words))
    filecov.write("Files Found Useful: " + str(parsed_files))
    filecov.write("Files Discarded: " + str(not_enough_words))
    filecov.write("Total Words: " + str(total_words))
    filecov.write("Cumulative covid score: " + str(total_covid_score))
    filecov.write("Bottom covid score: " + str(bottom_covid_score))
    filecov.write("Half covid score: " + str(half_covid_score))
    filecov.write("Low covid score: " + str(low_covid_score))
    filecov.write("High covid score: " + str(high_covid_score))
    filecov.write("Double covid score: " + str(two_covid_score))
    filecov.write("Top covid score: " + str(top_covid_score))
    filecov.write("Percentage of below bottom scores: " +
                  str(bottom_scores_per))
    filecov.write("Percentage of below half scores: " + str(half_scores_per))
    filecov.write("Percentage of below low scores: " + str(low_scores_per))
    filecov.write("Percentage of above high scores: " + str(high_scores_per))
    filecov.write("Percentage of above double scores: " + str(two_scores_per))
    filecov.write("Percentage of above top scores: " + str(top_scores_per))


# TODO: save files in subsets based on scores
