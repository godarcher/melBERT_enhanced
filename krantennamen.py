# The following program saves the info per krant as required

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

# set output paths
telegraaf_path = data_path + "\\" + "auteurs_telegraaf.csv"
ad_path = data_path + "\\" + "auteurs_ad.csv"
nrc_path = data_path + "\\" + "auteur_nrc.csv"
trouw_path = data_path + "\\" + "auteur_trouw.csv"
volkskrant_path = data_path + "\\" + "auteur_volkskrant.csv"

# reset all files
with open(telegraaf_path, 'w') as filecovr:
    filecovr.write("auteur,sectie,woorden,datum")
    filecovr.close()
with open(ad_path, 'w') as filecovr:
    filecovr.write("auteur,sectie,woorden,datum")
    filecovr.close()
with open(trouw_path, 'w') as filecovr:
    filecovr.write("auteur,sectie,woorden,datum")
    filecovr.close()
with open(volkskrant_path, 'w') as filecovr:
    filecovr.write("auteur,sectie,woorden,datum")
    filecovr.close()
with open(nrc_path, 'w') as filecovr:
    filecovr.write("auteur,sectie,woorden,datum")
    filecovr.close()


# For all files in data path
for filename in os.listdir(data_path):
    # If filename contains .txt and is metadata
    if filename.endswith(".txt") and filename.find("meta") != -1 and filename.find("metadata") == -1:
        # open file and read contents to string
        file_path = data_path + "\\" + filename
        # open the file with read permission
        with open(file_path, 'r', encoding='utf-8') as file:
            # We replace the newlines and make it lowercase
            data = file.read().replace('\n', '').lower()

            # +8 for length of "Length: "
            words_index = data.find("length:") + 8
            # this won't deliver problems because length is early in metadata
            words_end_index = data.find("words") - 1
            # cast to int to be able to do math with it
            words = int(data[words_index:words_end_index])

            # +8 for length of "Auteur: "
            auteur_index = data.find("auteur:") + 8
            auteur_end_index = 0
            auteur = ""

            if auteur_index != 7:
                # this won't deliver problems because length is early in metadata
                auteur_end_index = data.find("locatie") - 2
                # get actual metadata
                auteur = data[auteur_index:auteur_end_index]
            else:
                auteur_index = data.find("byline:") + 7
                if auteur_index != 6:
                    # this won't deliver problems because length is early in metadata
                    auteur_end_index = data.find("locatie") - 2
                    # get actual metadata
                    auteur = data[auteur_index:auteur_end_index]
                else:
                    auteur = "onbekend"

            # +8 for length of "Datum: "
            datum_index = data.find("datum:") + 7
            datum_end_index = data.find("section") - 2
            datum = data[datum_index:datum_end_index]

            # +9 for length of "Section: "
            section_index = data.find("section:") + 9
            section_end_index = data.find("length") - 2
            section = data[section_index:section_end_index]

            # check where the krant is from
            if filename.find("AD") != -1:
                with open(ad_path, 'a') as filecovr:
                    filecovr.write(auteur + "," + section +
                                   "," + str(words) + "," + datum + "\n")
                    filecovr.close()
            elif filename.find("NRC") != -1:
                with open(nrc_path, 'a') as filecovr:
                    filecovr.write(auteur + "," + section +
                                   "," + str(words) + "," + datum + "\n")
                    filecovr.close()
            elif filename.find("TELEGRAAF") != -1:
                with open(telegraaf_path, 'a') as filecovr:
                    filecovr.write(auteur + "," + section +
                                   "," + str(words) + "," + datum + "\n")
                    filecovr.close()
            elif filename.find("VOLKSKRANT") != -1:
                with open(volkskrant_path, 'a') as filecovr:
                    filecovr.write(auteur + "," + section +
                                   "," + str(words) + "," + datum + "\n")
                    filecovr.close()
            elif filename.find("TROUW") != -1:
                with open(trouw_path, 'a') as filecovr:
                    filecovr.write(auteur + "," + section +
                                   "," + str(words) + "," + datum + "\n")
                    filecovr.close()
