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
    filecovr.close()
with open(ad_path, 'w') as filecovr:
    filecovr.close()
with open(trouw_path, 'w') as filecovr:
    filecovr.close()
with open(volkskrant_path, 'w') as filecovr:
    filecovr.close()
with open(nrc_path, 'w') as filecovr:
    filecovr.close()

# For all files in data path
for filename in os.listdir(data_path):
    # If filename contains .txt and is metadata
    if filename.endswith(".txt") and filename.find("meta") != -1:
        # open file and read contents to string
        file_path = data_path + "\\" + filename

        # check where the krant is from
        if filename.find("AD") != -1:

        elif filename.find("NRC") != -1:

        elif filename.find("TELEGRAAF") != -1:

        elif filename.find("VOLKSKRANT") != -1:

        elif filename.find("TROUW") != -1:
