##############
# dependencies#
##############
import warnings
import csv
from lxml import etree
from io import StringIO, BytesIO
import os
import xml.etree.ElementTree as ET

###############
# DOCUMENTATION#
###############

################
# USER INTERFACE#
################

sentence_number = 0

###########
# FUNCTIONS#
###########
warnings.filterwarnings("ignore")


def findpos(child_of_child):

    # we maken een postag aan
    pos_tag = "empty"

    # ? Het correct taggen van werkwoorden, zelfstandige en bijvoeglijke naamwoorden.
    if "WW(" in child_of_child.get("pos"):
        pos_tag = "VERB"
    elif "N(" in child_of_child.get("pos"):
        pos_tag = "NOUN"
    elif "ADJ(" in child_of_child.get("pos"):
        pos_tag = "ADJ"

    # ? Het correct taggen van voornaamwoorden
    elif "VNW(" in child_of_child.get("pos") and "adv-pron" in child_of_child.get(
        "pos"
    ):
        pos_tag = "ADV"
    elif "VNW(" in child_of_child.get("pos") and "prenom" in child_of_child.get("pos"):
        pos_tag = "DET"
    elif (
        "VNW(" in child_of_child.get("pos")
        and "pron" in child_of_child.get("pos")
        and child_of_child.get("word").tolower() != "het"
    ):
        pos_tag = "PRON"

    # ? Het correct taggen van bijwoorden, lidwoorden en nummers
    elif "BW(" in child_of_child.get("pos"):
        pos_tag = "ADV"
    elif "LID(" in child_of_child.get("pos"):
        pos_tag = "DET"

    return pos_tag


def listdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


##################
# GLOBAL VARIABLES#
##################

filenumber = 0
parser = etree.XMLParser(ns_clean=True, remove_comments=True)
directory = r"C:\Users\Josso\Documents\Radboud\corpus_covid_parsed"

subdirectories = os.listdir(directory)
for directory_d2_first in subdirectories:
    print(directory_d2_first)
    directory_d2 = directory + "\\" + directory_d2_first

    outputdirectory = directory_d2.replace(".xml", "")
    outputindex = outputdirectory.rfind("\\")
    outputfolder = outputdirectory[outputindex + 1 :]
    outputfolder = outputfolder.replace("_sen.txt.alpinoxml", "")

    outputdirectory = outputdirectory + "\\" + outputfolder + "_" + "dev" + ".tsv"
    f = open(outputdirectory, "w", encoding="utf-8")

    # ? Added begin sentence of .csv file
    f.write("index	label	sentence	POS	w_index")

    context = ""
    context_counter = 0

    for filename in os.listdir(directory_d2):
        if filename.endswith(".xml"):

            filenumber = filenumber + 1

            # increment sentencenumber counter
            sentence_number = sentence_number + 1

            filedirectory = directory_d2 + "\\" + filename
            tree = etree.parse(filedirectory, parser)
            root = tree.getroot()

            sentence = ""

            ############################################
            # PART 1: get obj subj verb and sent number #
            ############################################
            for alpino_ds in root.iter("alpino_ds"):
                for top in alpino_ds:

                    # We test the sentence id's
                    sent_id = top.get("sentid")
                    if not str(sent_id) == "None":
                        sentence = top.text
                        if context_counter < 7:
                            context = context + " " + sentence
                            context_counter = context_counter + 1
                        else:
                            context_counter = 1
                            context = sentence

                        # ? Fix the sentence we just received
                        # escape csv problems
                        sentence = sentence.replace("\n", "")
                        # sentence fixes
                        if sentence.find(",") != -1 or sentence.find(";") != -1:
                            sentence = '"' + sentence + '"'
                        if sentence[0:1] == " ":
                            sentence = sentence[1:]

                    for smain in top:
                        ############
                        # MAIN LEVEL#
                        ############

                        for child in smain:
                            child_of_child = child.get("postag")
                            if not str(child_of_child) == "None":  # empty

                                pos = findpos(child_of_child)
                                if pos is not "empty":

                                    # ? Get word offset
                                    word = child_of_child.get("word")
                                    word_offset = sentence.rfind(word)

                                    #! Calculate and write output
                                    output = (
                                        "COV_fragment01"
                                        + " "
                                        + str(sentence_number)
                                        + "\t"
                                        + "0"
                                        + "\t"
                                        + str(sentence)
                                        + "\t"
                                        + pos
                                        + "\t"
                                        + str(word_offset)
                                    )
                                    f.write(output + "\n")

                            #########
                            # LEVEL 2#
                            #########

                            for childx in child:
                                child_of_child = childx.get("postag")
                                if not str(child_of_child) == "None":  # empty

                                    pos = findpos(child_of_child)
                                    if pos is not "empty":

                                        # ? Get word offset
                                        word = child_of_child.get("word")
                                        word_offset = sentence.rfind(word)

                                        #! Calculate and write output
                                        output = (
                                            "COV_fragment01"
                                            + " "
                                            + str(sentence_number)
                                            + "\t"
                                            + "0"
                                            + "\t"
                                            + str(sentence)
                                            + "\t"
                                            + pos
                                            + "\t"
                                            + str(word_offset)
                                        )
                                        f.write(output + "\n")

                                #########
                                # LEVEL 3#
                                #########

                                verbfound3 = False
                                for childy in childx:
                                    child_of_child = childy.get("postag")
                                    if not str(child_of_child) == "None":  # empty

                                        pos = findpos(child_of_child)
                                        if pos is not "empty":

                                            # ? Get word offset
                                            word = child_of_child.get("word")
                                            word_offset = sentence.rfind(word)

                                            #! Calculate and write output
                                            output = (
                                                "COV_fragment01"
                                                + " "
                                                + str(sentence_number)
                                                + "\t"
                                                + "0"
                                                + "\t"
                                                + str(sentence)
                                                + "\t"
                                                + pos
                                                + "\t"
                                                + str(word_offset)
                                            )
                                            f.write(output + "\n")

                                    #########
                                    # LEVEL 4#
                                    #########

                                    verbfound4 = False
                                    for childz in childy:
                                        kind_child = childz.get("pt")
                                        if not str(kind_child) == "None":  # empty
                                            if kind_child.find("ww") != -1:
                                                verbd4 = childz.get("word")
                                                # New: add verb lemma
                                                verbfound4 = True

                                    for childz in childy:
                                        if verbfound4 == True:
                                            rel_child = childz.get("rel")

                                        #########
                                        # LEVEL 5#
                                        #########

                                        verbfound5 = False
                                        for childa in childz:
                                            kind_child = childa.get("pt")
                                            if not str(kind_child) == "None":  # empty
                                                if kind_child.find("ww") != -1:
                                                    verbd5 = childa.get("word")
                                                    # New: add verb lemma
                                                    verbfound5 = True

                                        for childa in childz:
                                            if verbfound5 == True:
                                                rel_child = childa.get("rel")

                                            #########
                                            # LEVEL 6#
                                            #########

                                            verbfound6 = False
                                            for childb in childa:
                                                kind_child = childb.get("pt")
                                                if (
                                                    not str(kind_child) == "None"
                                                ):  # empty
                                                    if kind_child.find("ww") != -1:
                                                        verbd6 = childb.get("word")
                                                        verbfound6 = True

                                            for childb in childa:
                                                if verbfound6 == True:
                                                    rel_child = childb.get("rel")

                                                #########
                                                # LEVEL 7#
                                                #########

                                                verbfound7 = False
                                                for childc in childb:
                                                    kind_child = childc.get("pt")
                                                    if (
                                                        not str(kind_child) == "None"
                                                    ):  # empty
                                                        if kind_child.find("ww") != -1:
                                                            verbd7 = childc.get("word")
                                                            verbfound7 = True

                                                for childc in childb:
                                                    if verbfound7 == True:
                                                        rel_child = childc.get("rel")

    f.close()
