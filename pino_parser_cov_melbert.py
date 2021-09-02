##############
#dependencies#
##############
import warnings
import csv
from lxml import etree
from io import StringIO, BytesIO
import os
import xml.etree.ElementTree as ET

###############
#DOCUMENTATION#
###############

################
#USER INTERFACE#
################

# globals
verbd1 = ""
verbd2 = ""
verbd3 = ""
verbd4 = ""
verbd5 = ""
verbd6 = ""
verbd7 = ""

verbd1lemma = ""
verbd2lemma = ""
verbd3lemma = ""
verbd4lemma = ""
verbd5lemma = ""
verbd6lemma = ""
verbd7lemma = ""

objd1 = ""
objd2 = ""
objd3 = ""
objd4 = ""
objd5 = ""
objd6 = ""
objd7 = ""

olemd1 = ""
olemd2 = ""
olemd3 = ""
olemd4 = ""
olemd5 = ""
olemd6 = ""
olemd7 = ""

subd1 = ""
subd2 = ""
subd3 = ""
subd4 = ""
subd5 = ""
subd6 = ""
subd7 = ""

slemd1 = ""
slemd2 = ""
slemd3 = ""
slemd4 = ""
slemd5 = ""
slemd6 = ""
slemd7 = ""

temp_lemma = ""

debug = True

sentence_number = 0

###########
#FUNCTIONS#
###########
warnings.filterwarnings("ignore")


def listdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


def find_cor_index(index, currentchild, d, isobject):
    for alpino_ds in root.iter('alpino_ds'):
        for top in alpino_ds:
            for smain in top:
                for child in smain:
                    # D1
                    ind_child = child.get('index')
                    if not str(ind_child) == "None":  # empty
                        if ind_child == index and child != currentchild:
                            if not str(child.get('word')) == "None" or child:
                                touse = find_linked_object(child, d, isobject)
                    # D2
                    for child2 in child:
                        ind_child = child2.get('index')
                        if not str(ind_child) == "None":  # empty
                            if ind_child == index and child2 != currentchild:
                                if not str(child2.get('word')) == "None" or child2:
                                    touse = find_linked_object(
                                        child2, d, isobject)
                    # D3
                        for child3 in child2:
                            ind_child = child3.get('index')
                            if not str(ind_child) == "None":  # empty
                                if ind_child == index and child3 != currentchild:
                                    if not str(child3.get('word')) == "None" or child3:
                                        touse = find_linked_object(
                                            child3, d, isobject)
                    # D4
                            for child4 in child3:
                                ind_child = child4.get('index')
                                if not str(ind_child) == "None":  # empty
                                    if ind_child == index and child4 != currentchild:
                                        if not str(child4.get('word')) == "None" or child4:
                                            touse = find_linked_object(
                                                child4, d, isobject)

                    # D5
                                for child5 in child4:
                                    ind_child = child5.get('index')
                                    if not str(ind_child) == "None":  # empty
                                        if ind_child == index and child5 != currentchild:
                                            if not str(child5.get('word')) == "None" or child5:
                                                touse = find_linked_object(
                                                    child5, d, isobject)

                    # D6
                                    for child6 in child5:
                                        ind_child = child6.get('index')
                                        if not str(ind_child) == "None":  # empty
                                            if ind_child == index and child6 != currentchild:
                                                if not str(child6.get('word')) == "None" or child6:
                                                    touse = find_linked_object(
                                                        child6, d, isobject)
                    # D7
                                        for child7 in child6:
                                            ind_child = child7.get('index')
                                            if not str(ind_child) == "None":  # empty
                                                if ind_child == index and child7 != currentchild:
                                                    if not str(child7.get('word')) == "None" or child7:
                                                        touse = find_linked_object(
                                                            child7, d, isobject)
                    # D8
                                            for child8 in child7:
                                                ind_child = child8.get('index')
                                                if not str(ind_child) == "None":  # empty
                                                    if ind_child == index and child8 != currentchild:
                                                        if not str(child8.get('word')) == "None" or child8:
                                                            touse = find_linked_object(
                                                                child8, d, isobject)


def find_linked_object(child, d, isobject):
    output = find_linked_object2(child)
    if isobject == True:
        # object
        global temp_lemma
        if d == 1:
            global objd1
            objd1 = output
            global olemd1
            oldemd1 = temp_lemma
        elif d == 2:
            global objd2
            objd2 = output
            global olemd2
            olemd2 = temp_lemma
        elif d == 3:
            global objd3
            objd3 = output
            global olemd3
            olemd3 = temp_lemma
        elif d == 4:
            global objd4
            objd4 = output
            global olemd4
            olemd4 = temp_lemma
        elif d == 5:
            global objd5
            objd5 = output
            global olemd5
            olemd5 = temp_lemma
        elif d == 6:
            global objd6
            objd6 = output
            global olemd6
            olemd6 = temp_lemma
        elif d == 7:
            global objd7
            objd7 = output
            global olemd7
            olemd7 = temp_lemma
    else:
        # subject
        if d == 1:
            global subd1
            global slemd1
            slemd1 = temp_lemma
            subd1 = output
        elif d == 2:
            global subd2
            subd2 = output
            global slemd2
            slemd2 = temp_lemma
        elif d == 3:
            global subd3
            subd3 = output
            global slemd3
            slemd3 = temp_lemma
        elif d == 4:
            global subd4
            subd4 = output
            global slemd4
            slemd4 = temp_lemma
        elif d == 5:
            global subd5
            subd5 = output
            global slemd5
            slemd5 = temp_lemma
        elif d == 6:
            global subd6
            subd6 = output
            global slemd6
            slemd6 = temp_lemma
        elif d == 7:
            global subd7
            subd7 = output
            global slemd7
            slemd7 = temp_lemma


def find_linked_object2(child):
    # input child node
    # output --> iterates over 4 dimensions of childs of child and child itself to find core of object/subject

    global temp_lemma

    # D1 (from object)
    word_in_child = child.get('pt')
    if not str(word_in_child) == "None":
        if word_in_child == "n" or word_in_child == "vnw":
            # found highest noun
            # first get lemma
            temp_lemma = child.get('lemma')
            return child.get('word')

    # D2
    temp_lemma = ""
    d_obj = ""

    # never reached
    for child2 in child:
        word_in_child = child2.get('pt')
        if not str(word_in_child) == "None":
            if word_in_child == "n" or word_in_child == "vnw":
                # found highest noun
                if d_obj == "":
                    temp_lemma = child2.get('lemma')
                    d_obj = child2.get('word')
                else:
                    temp_lemma = temp_lemma + child2.get('lemma')
                    d_obj = d_obj + " " + child2.get('word')

        if d_obj != "":
            return d_obj

    # D3
        d_obj = ""
        temp_lemma = ""
        for child3 in child2:
            word_in_child = child3.get('pt')
            if not str(word_in_child) == "None":
                if word_in_child == "n" or word_in_child == "vnw":
                    # found highest noun
                    if d_obj == "":
                        temp_lemma = child3.get('word')
                        d_obj = child3.get('word')
                    else:
                        temp_lemma = temp_lemma + child3.get('lemma')
                        d_obj = d_obj + " " + child3.get('word')

            if d_obj != "":
                return d_obj

    # D4
            d_obj = ""
            temp_lemma = ""
            for child4 in child3:
                word_in_child = child4.get('pt')
                if not str(word_in_child) == "None":
                    if word_in_child == "n" or word_in_child == "vnw":
                        # found highest noun
                        if d_obj == "":
                            temp_lemma = child4.get('word')
                            d_obj = child4.get('word')
                        else:
                            temp_lemma = temp_lemma + child4.get('lemma')
                            d_obj = d_obj + " " + child4.get('word')

                if d_obj != "":
                    return d_obj

    # D5
                d_obj = ""
                temp_lemma = ""
                for child5 in child4:
                    word_in_child = child5.get('pt')
                    if not str(word_in_child) == "None":
                        if word_in_child == "n" or word_in_child == "vnw":
                            # found highest noun
                            if d_obj == "":
                                temp_lemma = child5.get('word')
                                d_obj = child5.get('word')
                            else:
                                temp_lemma = temp_lemma + child5.get('lemma')
                                d_obj = d_obj + " " + child5.get('word')

                    if d_obj != "":
                        return d_obj

    # D6
                    d_obj = ""
                    temp_lemma = ""
                    for child6 in child5:
                        word_in_child = child6.get('pt')
                        if not str(word_in_child) == "None":
                            if word_in_child == "n" or word_in_child == "vnw":
                                # found highest noun
                                if d_obj == "":
                                    temp_lemma = child6.get('word')
                                    d_obj = child6.get('word')
                                else:
                                    temp_lemma = temp_lemma + \
                                        child6.get('lemma')
                                    d_obj = d_obj + " " + child6.get('word')

                        if d_obj != "":
                            return d_obj
##################
#GLOBAL VARIABLES#
##################


filenumber = 0
parser = etree.XMLParser(ns_clean=True, remove_comments=True)
directory = r'C:\Users\Josso\Documents\Radboud\corpus_covid_parsed'

subdirectories = os.listdir(directory)
for directory_d2_first in subdirectories:
    print(directory_d2_first)
    directory_d2 = directory + "\\" + directory_d2_first

    outputdirectory = directory_d2.replace(".xml", "")
    outputindex = outputdirectory.rfind("\\")
    outputfolder = outputdirectory[outputindex+1:]
    outputfolder = outputfolder.replace("_sen.txt.alpinoxml", "")

    outputdirectory = outputdirectory + "\\" + \
        outputfolder + "_" + "dev" + ".tsv"
    f = open(outputdirectory, "w", encoding="utf-8")

    #? Added begin sentence of .csv file
    f.write("index	label	sentence	POS	w_index")

    context = ""
    context_counter = 0

    for filename in os.listdir(directory_d2):
        if filename.endswith(".xml"):
            # print(filename)
            # definitions are placed here so they are reset for each file
            verbd1 = ""
            verbd2 = ""
            verbd3 = ""
            verbd4 = ""
            verbd5 = ""
            verbd6 = ""
            verbd7 = ""

            verbd1lemma = ""
            verbd2lemma = ""
            verbd3lemma = ""
            verbd4lemma = ""
            verbd5lemma = ""
            verbd6lemma = ""
            verbd7lemma = ""

            objd1 = ""
            objd2 = ""
            objd3 = ""
            objd4 = ""
            objd5 = ""
            objd6 = ""
            objd7 = ""

            olemd1 = ""
            olemd2 = ""
            olemd3 = ""
            olemd4 = ""
            olemd5 = ""
            olemd6 = ""
            olemd7 = ""

            subd1 = ""
            subd2 = ""
            subd3 = ""
            subd4 = ""
            subd5 = ""
            subd6 = ""
            subd7 = ""

            slemd1 = ""
            slemd2 = ""
            slemd3 = ""
            slemd4 = ""
            slemd5 = ""
            slemd6 = ""
            slemd7 = ""

            filenumber = filenumber + 1

            # increment sentencenumber counter
            sentence_number = sentence_number + 1

            filedirectory = directory_d2 + "\\" + filename
            tree = etree.parse(filedirectory, parser)
            root = tree.getroot()

            sentence = ""

            ############################################
            #PART 1: get obj subj verb and sent number #
            ############################################
            for alpino_ds in root.iter('alpino_ds'):
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

                    for smain in top:
                        verbfound = False

                        ############
                        #MAIN LEVEL#
                        ############

                        for child in smain:
                            kind_child = child.get('pt')
                            if not str(kind_child) == "None":  # empty
                                if kind_child.find('ww') != -1:
                                    verbd1 = child.get('word')
                                    # New: add verb lemma
                                    verbd1lemma = child.get('lemma')
                                    verbfound = True

                        for child in smain:
                            if verbfound == True:
                                rel_child = child.get('rel')
                                # Gather object
                                if not str(rel_child) == "None":  # empty
                                    if rel_child.find('obj1') != -1:
                                        word_in_child = child.get('pt')
                                        if not str(word_in_child) == "None":
                                            if word_in_child == "n" or word_in_child == "vnw":
                                                # found highest noun
                                                objd1 = child.get('word')
                                                olemd1 = child.get('lemma')
                                        for child2 in child:
                                            rel_child = child2.get('pt')
                                            if not str(rel_child) == "None":  # empty
                                                # level deeper
                                                word_in_child = child2.get(
                                                    'pt')
                                                if not str(word_in_child) == "None":
                                                    if word_in_child == "n" or word_in_child == "vnw":
                                                        # found highest noun
                                                        if objd1 == "":
                                                            olemd1 = child2.get(
                                                                'lemma')
                                                            objd1 = child2.get(
                                                                'word')
                                                        else:
                                                            olemd1 = olemd1 + " " + \
                                                                child2.get(
                                                                    'lemma')
                                                            objd1 = objd1 + " " + \
                                                                child2.get(
                                                                    'word')
                                # no result yet? --> check index (dependent one)
                                if objd1 == "" and not child and rel_child.find('obj1') != -1:
                                    ind_child = child.get('index')
                                    if not str(ind_child) == "None":  # empty
                                        find_cor_index(
                                            ind_child, child, 1, True)

                                rel_child = child.get('rel')
                                # Gather subject
                                if not str(rel_child) == "None":  # empty
                                    if rel_child.find('su') != -1:
                                        word_in_child = child.get('pt')
                                        if not str(word_in_child) == "None":
                                            if word_in_child == "n" or word_in_child == "vnw":
                                                # found highest noun
                                                slemd1 = child.get('lemma')
                                                subd1 = child.get('word')
                                        for child2 in child:
                                            rel_child = child2.get('rel')
                                            if not str(rel_child) == "None":  # empty
                                                # level deeper
                                                word_in_child = child2.get(
                                                    'pt')
                                                if not str(word_in_child) == "None":
                                                    if word_in_child == "n" or word_in_child == "vnw":
                                                        # found highest noun
                                                        if subd1 == "":
                                                            slemd1 = child2.get(
                                                                'lemma')
                                                            subd1 = child2.get(
                                                                'word')
                                                        else:
                                                            slemd1 = slemd1 + " " + \
                                                                child2.get(
                                                                    'lemma')
                                                            subd1 = subd1 + " " + \
                                                                child2.get(
                                                                    'word')

                                # no result yet? --> check index (dependent one)
                                if subd1 == "" and not child and rel_child.find('su') != -1:
                                    ind_child = child.get('index')
                                    if not str(ind_child) == "None":  # empty
                                        find_cor_index(
                                            ind_child, child, 1, False)

                        #########
                        #LEVEL 2#
                        #########

                            verbfound2 = False
                            for childx in child:
                                kind_child = childx.get('pt')
                                if not str(kind_child) == "None":  # empty
                                    if kind_child.find('ww') != -1:
                                        verbd2 = childx.get('word')
                                        # New: add verb lemma
                                        verbd2lemma = childx.get('lemma')
                                        verbfound2 = True

                            for childx in child:
                                if verbfound2 == True:
                                    rel_child = childx.get('rel')
                                    # Gather object
                                    if not str(rel_child) == "None":  # empty
                                        if rel_child.find('obj1') != -1:
                                            word_in_child = childx.get('pt')
                                            if not str(word_in_child) == "None":
                                                if word_in_child == "n" or word_in_child == "vnw":
                                                    # found highest noun
                                                    olemd2 = childx.get(
                                                        'lemma')
                                                    objd2 = childx.get('word')
                                            for child2 in childx:
                                                rel_child = child2.get('pt')
                                                if not str(rel_child) == "None":  # empty
                                                    # level deeper
                                                    word_in_child = child2.get(
                                                        'pt')
                                                    if not str(word_in_child) == "None":
                                                        if word_in_child == "n" or word_in_child == "vnw":
                                                            # found highest noun
                                                            if objd2 == "":
                                                                olemd2 = child2.get(
                                                                    'lemma')
                                                                objd2 = child2.get(
                                                                    'word')
                                                            else:
                                                                olemd2 = olemd2 + " " + \
                                                                    child2.get(
                                                                        'lemma')
                                                                objd2 = objd2 + " " + \
                                                                    child2.get(
                                                                        'word')
                                    # no result yet? --> check index (dependent one)
                                    if objd2 == "" and not childx and rel_child.find('obj1') != -1:
                                        ind_child = childx.get('index')
                                        if not str(ind_child) == "None":  # empty
                                            find_cor_index(
                                                ind_child, childx, 2, True)

                                    rel_child = childx.get('rel')
                                    # Gather subject
                                    if not str(rel_child) == "None":  # empty
                                        if rel_child.find('su') != -1:
                                            word_in_child = childx.get('pt')
                                            if not str(word_in_child) == "None":
                                                if word_in_child == "n" or word_in_child == "vnw":
                                                    # found highest noun
                                                    subd2 = childx.get('word')
                                                    slemd2 = childx.get(
                                                        'lemma')
                                            for child2 in childx:
                                                rel_child = child2.get('rel')
                                                if not str(rel_child) == "None":  # empty
                                                    # level deeper
                                                    word_in_child = child2.get(
                                                        'pt')
                                                    if not str(word_in_child) == "None":
                                                        if word_in_child == "n" or word_in_child == "vnw":
                                                            # found highest noun
                                                            if subd2 == "":
                                                                subd2 = child2.get(
                                                                    'word')
                                                                slemd2 = child2.get(
                                                                    'lemma')
                                                            else:
                                                                subd2 = subd2 + " " + \
                                                                    child2.get(
                                                                        'word')
                                                                slemd2 = slemd2 + " " + \
                                                                    child2.get(
                                                                        'lemma')
                                    # no result yet? --> check index (dependent one)
                                    if subd2 == "" and not childx and rel_child.find('su') != -1:
                                        ind_child = childx.get('index')
                                        if not str(ind_child) == "None":  # empty
                                            find_cor_index(
                                                ind_child, childx, 2, False)

                        #########
                        #LEVEL 3#
                        #########

                                verbfound3 = False
                                for childy in childx:
                                    kind_child = childy.get('pt')
                                    if not str(kind_child) == "None":  # empty
                                        if kind_child.find('ww') != -1:
                                            verbd3 = childy.get('word')
                                            # New: add verb lemma
                                            verbd3lemma = childy.get('lemma')
                                            verbfound3 = True

                                for childy in childx:
                                    if verbfound3 == True:
                                        rel_child = childy.get('rel')
                                        # Gather object
                                        if not str(rel_child) == "None":  # empty
                                            if rel_child.find('obj1') != -1:
                                                word_in_child = childy.get(
                                                    'pt')
                                                if not str(word_in_child) == "None":
                                                    if word_in_child == "n" or word_in_child == "vnw":
                                                        # found highest noun
                                                        objd3 = childy.get(
                                                            'word')
                                                        olemd3 = childy.get(
                                                            'lemma')
                                                for child2 in childy:
                                                    rel_child = child2.get(
                                                        'pt')
                                                    if not str(rel_child) == "None":  # empty
                                                        # level deeper
                                                        word_in_child = child2.get(
                                                            'pt')
                                                        if not str(word_in_child) == "None":
                                                            if word_in_child == "n" or word_in_child == "vnw":
                                                                # found highest noun
                                                                if objd3 == "":
                                                                    olemd3 = child2.get(
                                                                        'lemma')
                                                                    objd3 = child2.get(
                                                                        'word')
                                                                else:
                                                                    olemd3 = olemd3 + " " + \
                                                                        child2.get(
                                                                            'lemma')
                                                                    objd3 = objd3 + " " + \
                                                                        child2.get(
                                                                            'word')
                                        # no result yet? --> check index (dependent one)
                                        if objd3 == "" and not childy and rel_child.find('obj1') != -1:
                                            ind_child = childy.get('index')
                                            if not str(ind_child) == "None":  # empty
                                                find_cor_index(
                                                    ind_child, childy, 3, True)

                                        rel_child = childy.get('rel')
                                        # Gather subject
                                        if not str(rel_child) == "None":  # empty
                                            if rel_child.find('su') != -1:
                                                word_in_child = childy.get(
                                                    'pt')
                                                if not str(word_in_child) == "None":
                                                    if word_in_child == "n" or word_in_child == "vnw":
                                                        # found highest noun
                                                        if not str(childy.get('word')) == "None":
                                                            subd3 = childy.get(
                                                                'word')
                                                            slemd3 = childy.get(
                                                                'lemma')

                                                for child2 in childy:
                                                    rel_child = child2.get(
                                                        'rel')
                                                    if not str(rel_child) == "None":  # empty
                                                        # level deeper
                                                        word_in_child = child2.get(
                                                            'pt')
                                                        if not str(word_in_child) == "None":
                                                            if word_in_child == "n" or word_in_child == "vnw":
                                                                # found highest noun
                                                                if subd3 == "" or str(subd3) == "None":
                                                                    subd3 = child2.get(
                                                                        'word')
                                                                    slemd3 = child2.get(
                                                                        'lemma')
                                                                else:
                                                                    subd3 = subd3 + " " + \
                                                                        child2.get(
                                                                            'word')
                                                                    slemd3 = slemd3 + " " + \
                                                                        child2.get(
                                                                            'lemma')
                                        # no result yet? --> check index (dependent one)
                                        if subd3 == "" and not childy and rel_child.find('su') != -1:
                                            ind_child = childy.get('index')
                                            if not str(ind_child) == "None":  # empty)
                                                find_cor_index(
                                                    ind_child, childy, 3, False)

                        #########
                        #LEVEL 4#
                        #########

                                    verbfound4 = False
                                    for childz in childy:
                                        kind_child = childz.get('pt')
                                        if not str(kind_child) == "None":  # empty
                                            if kind_child.find('ww') != -1:
                                                verbd4 = childz.get('word')
                                                # New: add verb lemma
                                                verbd4lemma = childz.get(
                                                    'lemma')
                                                verbfound4 = True

                                    for childz in childy:
                                        if verbfound4 == True:
                                            rel_child = childz.get('rel')
                                            # Gather object
                                            if not str(rel_child) == "None":  # empty
                                                if rel_child.find('obj1') != -1:
                                                    word_in_child = childz.get(
                                                        'pt')
                                                    if not str(word_in_child) == "None":
                                                        if word_in_child == "n" or word_in_child == "vnw":
                                                            # found highest noun
                                                            objd4 = childz.get(
                                                                'word')
                                                            olemd4 = childz.get(
                                                                'lemma')
                                                    for child2 in childz:
                                                        rel_child = child2.get(
                                                            'pt')
                                                        if not str(rel_child) == "None":  # empty
                                                            # level deeper
                                                            word_in_child = child2.get(
                                                                'pt')
                                                            if not str(word_in_child) == "None":
                                                                if word_in_child == "n" or word_in_child == "vnw":
                                                                    # found highest noun
                                                                    if objd4 == "":
                                                                        objd4 = child2.get(
                                                                            'word')
                                                                        olemd4 = child2.get(
                                                                            'lemma')
                                                                    else:
                                                                        olemd4 = olemd4 + " " + \
                                                                            child2.get(
                                                                                'lemma')
                                                                        objd4 = objd4 + " " + \
                                                                            child2.get(
                                                                                'word')
                                            # no result yet? --> check index (dependent one)
                                            if objd4 == "" and not childz and rel_child.find('obj1') != -1:
                                                ind_child = childz.get('index')
                                                if not str(ind_child) == "None":  # empty
                                                    find_cor_index(
                                                        ind_child, childz, 4, True)

                                            rel_child = childz.get('rel')
                                            # Gather subject
                                            if not str(rel_child) == "None":  # empty
                                                if rel_child.find('su') != -1:
                                                    word_in_child = childz.get(
                                                        'pt')
                                                    if not str(word_in_child) == "None":
                                                        if word_in_child == "n" or word_in_child == "vnw":
                                                            # found highest noun
                                                            subd4 = childz.get(
                                                                'word')
                                                            slemd4 = childz.get(
                                                                'lemma')
                                                    for child2 in childz:
                                                        rel_child = child2.get(
                                                            'rel')
                                                        if not str(rel_child) == "None":  # empty
                                                            # level deeper
                                                            word_in_child = child2.get(
                                                                'pt')
                                                            if not str(word_in_child) == "None":
                                                                if word_in_child == "n" or word_in_child == "vnw":
                                                                    # found highest noun
                                                                    if subd4 == "" or str(subd4) == "None":
                                                                        subd4 = child2.get(
                                                                            'word')
                                                                        slemd4 = child2.get(
                                                                            'lemma')
                                                                    else:
                                                                        subd4 = subd4 + " " + \
                                                                            child2.get(
                                                                                'word')
                                                                        slemd4 = slemd4 + " " + \
                                                                            child2.get(
                                                                                'lemma')
                                            # no result yet? --> check index (dependent one)
                                            if subd4 == "" and not childz and rel_child.find('su') != -1:
                                                ind_child = childz.get('index')
                                                if not str(ind_child) == "None":  # empty
                                                    find_cor_index(
                                                        ind_child, childz, 4, False)

                        #########
                        #LEVEL 5#
                        #########

                                        verbfound5 = False
                                        for childa in childz:
                                            kind_child = childa.get('pt')
                                            if not str(kind_child) == "None":  # empty
                                                if kind_child.find('ww') != -1:
                                                    verbd5 = childa.get('word')
                                                    # New: add verb lemma
                                                    verbd5lemma = childa.get(
                                                        'lemma')
                                                    verbfound5 = True

                                        for childa in childz:
                                            if verbfound5 == True:
                                                rel_child = childa.get('rel')
                                                # Gather object
                                                if not str(rel_child) == "None":  # empty
                                                    if rel_child.find('obj1') != -1:
                                                        word_in_child = childa.get(
                                                            'pt')
                                                        if not str(word_in_child) == "None":
                                                            if word_in_child == "n" or word_in_child == "vnw":
                                                                # found highest noun
                                                                objd5 = childa.get(
                                                                    'word')
                                                                olemd5 = childa.get(
                                                                    'lemma')
                                                        for child2 in childa:
                                                            rel_child = child2.get(
                                                                'pt')
                                                            # empty
                                                            if not str(rel_child) == "None":
                                                                # level deeper
                                                                word_in_child = child2.get(
                                                                    'pt')
                                                                if not str(word_in_child) == "None":
                                                                    if word_in_child == "n" or word_in_child == "vnw":
                                                                        # found highest noun
                                                                        if objd5 == "":
                                                                            olemd5 = child2.get(
                                                                                'lemma')
                                                                            objd5 = child2.get(
                                                                                'word')
                                                                        else:
                                                                            olemd5 = olemd5 + " " + \
                                                                                child2.get(
                                                                                    'lemma')
                                                                            objd5 = objd5 + " " + \
                                                                                child2.get(
                                                                                    'word')
                                                # no result yet? --> check index (dependent one)
                                                if objd5 == "" and not childa and rel_child.find('obj1') != -1:
                                                    ind_child = childa.get(
                                                        'index')
                                                    if not str(ind_child) == "None":  # empty
                                                        find_cor_index(
                                                            ind_child, childa, 5, True)

                                                rel_child = childa.get('rel')
                                                # Gather subject
                                                if not str(rel_child) == "None":  # empty
                                                    if rel_child.find('su') != -1:
                                                        word_in_child = childa.get(
                                                            'pt')
                                                        if not str(word_in_child) == "None":
                                                            if word_in_child == "n" or word_in_child == "vnw":
                                                                # found highest noun
                                                                subd5 = childa.get(
                                                                    'word')
                                                                slemd5 = childa.get(
                                                                    'lemma')
                                                        for child2 in childa:
                                                            rel_child = child2.get(
                                                                'rel')
                                                            # empty
                                                            if not str(rel_child) == "None":
                                                                # level deeper
                                                                word_in_child = child2.get(
                                                                    'pt')
                                                                if not str(word_in_child) == "None":
                                                                    if word_in_child == "n" or word_in_child == "vnw":
                                                                        # found highest noun
                                                                        if subd5 == "":
                                                                            subd5 = child2.get(
                                                                                'word')
                                                                            slemd5 = child2.get(
                                                                                'lemma')
                                                                        else:
                                                                            subd5 = subd5 + " " + \
                                                                                child2.get(
                                                                                    'word')
                                                                            slemd5 = slemd5 + " " + \
                                                                                child2.get(
                                                                                    'lemma')
                                                # no result yet? --> check index (dependent one)
                                                if subd5 == "" and not childa and rel_child.find('su') != -1:
                                                    ind_child = childa.get(
                                                        'index')
                                                    if not str(ind_child) == "None":  # empty
                                                        find_cor_index(
                                                            ind_child, childa, 5, False)

                        #########
                        #LEVEL 6#
                        #########

                                            verbfound6 = False
                                            for childb in childa:
                                                kind_child = childb.get('pt')
                                                if not str(kind_child) == "None":  # empty
                                                    if kind_child.find('ww') != -1:
                                                        verbd6 = childb.get(
                                                            'word')
                                                        # New: add verb lemma
                                                        verbd6lemma = childb.get(
                                                            'lemma')
                                                        verbfound6 = True

                                            for childb in childa:
                                                if verbfound6 == True:
                                                    rel_child = childb.get(
                                                        'rel')
                                                    # Gather object
                                                    if not str(rel_child) == "None":  # empty
                                                        if rel_child.find('obj1') != -1:
                                                            word_in_child = childb.get(
                                                                'pt')
                                                            if not str(word_in_child) == "None":
                                                                if word_in_child == "n" or word_in_child == "vnw":
                                                                    # found highest noun
                                                                    olemd6 = childb.get(
                                                                        'lemma')
                                                                    objd6 = childb.get(
                                                                        'word')
                                                            for child2 in childb:
                                                                rel_child = child2.get(
                                                                    'pt')
                                                                # empty
                                                                if not str(rel_child) == "None":
                                                                    # level deeper
                                                                    word_in_child = child2.get(
                                                                        'pt')
                                                                    if not str(word_in_child) == "None":
                                                                        if word_in_child == "n" or word_in_child == "vnw":
                                                                            # found highest noun
                                                                            if objd6 == "":
                                                                                olemd6 = child2.get(
                                                                                    'lemma')
                                                                                objd6 = child2.get(
                                                                                    'word')
                                                                            else:
                                                                                olemd6 = olemd6 + " " + \
                                                                                    child2.get(
                                                                                        'lemma')
                                                                                objd6 = objd6 + " " + \
                                                                                    child2.get(
                                                                                        'word')
                                                    # no result yet? --> check index (dependent one)
                                                    if objd6 == "" and not childb and rel_child.find('obj1') != -1:
                                                        ind_child = childb.get(
                                                            'index')
                                                        if not str(ind_child) == "None":  # empty
                                                            find_cor_index(
                                                                ind_child, childb, 6, True)

                                                    rel_child = childb.get(
                                                        'rel')
                                                    # Gather subject
                                                    if not str(rel_child) == "None":  # empty
                                                        if rel_child.find('su') != -1:
                                                            word_in_child = childb.get(
                                                                'pt')
                                                            if not str(word_in_child) == "None":
                                                                if word_in_child == "n" or word_in_child == "vnw":
                                                                    # found highest noun
                                                                    subd6 = childb.get(
                                                                        'word')
                                                                    slemd6 = childb.get(
                                                                        'lemma')
                                                            for child2 in childb:
                                                                rel_child = child2.get(
                                                                    'rel')
                                                                # empty
                                                                if not str(rel_child) == "None":
                                                                    # level deeper
                                                                    word_in_child = child2.get(
                                                                        'pt')
                                                                    if not str(word_in_child) == "None":
                                                                        if word_in_child == "n" or word_in_child == "vnw":
                                                                            # found highest noun
                                                                            if subd6 == "":
                                                                                subd6 = child2.get(
                                                                                    'word')
                                                                                slemd6 = child2.get(
                                                                                    'lemma')
                                                                            else:
                                                                                subd6 = subd6 + " " + \
                                                                                    child2.get(
                                                                                        'word')
                                                                                slemd6 = slemd6 + " " + \
                                                                                    child2.get(
                                                                                        'lemma')
                                                    # no result yet? --> check index (dependent one)
                                                    if subd6 == "" and not childb and rel_child.find('su') != -1:
                                                        ind_child = childb.get(
                                                            'index')
                                                        if not str(ind_child) == "None":  # empty
                                                            find_cor_index(
                                                                ind_child, childb, 6, False)

                        #########
                        #LEVEL 7#
                        #########

                                                verbfound7 = False
                                                for childc in childb:
                                                    kind_child = childc.get(
                                                        'pt')
                                                    if not str(kind_child) == "None":  # empty
                                                        if kind_child.find('ww') != -1:
                                                            verbd7 = childc.get(
                                                                'word')
                                                            # New: add verb lemma
                                                            verbd7lemma = childc.get(
                                                                'lemma')
                                                            verbfound7 = True

                                                for childc in childb:
                                                    if verbfound7 == True:
                                                        rel_child = childc.get(
                                                            'rel')
                                                        # Gather object
                                                        if not str(rel_child) == "None":  # empty
                                                            if rel_child.find('obj1') != -1:
                                                                word_in_child = childc.get(
                                                                    'pt')
                                                                if not str(word_in_child) == "None":
                                                                    if word_in_child == "n" or word_in_child == "vnw":
                                                                        # found highest noun
                                                                        olemd7 = childc.get(
                                                                            'lemma')
                                                                        objd7 = childc.get(
                                                                            'word')
                                                                for child2 in childc:
                                                                    rel_child = child2.get(
                                                                        'pt')
                                                                    # empty
                                                                    if not str(rel_child) == "None":
                                                                        # level deeper
                                                                        word_in_child = child2.get(
                                                                            'pt')
                                                                        if not str(word_in_child) == "None":
                                                                            if word_in_child == "n" or word_in_child == "vnw":
                                                                                # found highest noun
                                                                                if objd7 == "":
                                                                                    olemd7 = child2.get(
                                                                                        'lemma')
                                                                                    objd7 = child2.get(
                                                                                        'word')
                                                                                else:
                                                                                    olemd7 = olemd7 + " " + \
                                                                                        child2.get(
                                                                                            'lemma')
                                                                                    objd7 = objd7 + " " + \
                                                                                        child2.get(
                                                                                            'word')
                                                        # no result yet? --> check index (dependent one)
                                                        if objd7 == "" and not childc and rel_child.find('obj1') != -1:
                                                            ind_child = childc.get(
                                                                'index')
                                                            # empty
                                                            if not str(ind_child) == "None":
                                                                find_cor_index(
                                                                    ind_child, childc, 7, True)

                                                        rel_child = childc.get(
                                                            'rel')
                                                        # Gather subject
                                                        if not str(rel_child) == "None":  # empty
                                                            if rel_child.find('su') != -1:
                                                                word_in_child = childc.get(
                                                                    'pt')
                                                                if not str(word_in_child) == "None":
                                                                    if word_in_child == "n" or word_in_child == "vnw":
                                                                        # found highest noun
                                                                        subd7 = childc.get(
                                                                            'word')
                                                                        slemd7 = childc.get(
                                                                            'lemma')
                                                                for child2 in childc:
                                                                    rel_child = child2.get(
                                                                        'rel')
                                                                    # empty
                                                                    if not str(rel_child) == "None":
                                                                        # level deeper
                                                                        word_in_child = child2.get(
                                                                            'pt')
                                                                        if not str(word_in_child) == "None":
                                                                            if word_in_child == "n" or word_in_child == "vnw":
                                                                                # found highest noun
                                                                                if subd7 == "":
                                                                                    subd7 = child2.get(
                                                                                        'word')
                                                                                    slemd7 = child2.get(
                                                                                        'lemma')
                                                                                else:
                                                                                    subd7 = subd7 + " " + \
                                                                                        child2.get(
                                                                                            'word')
                                                                                    slemd7 = slemd7 + " " + \
                                                                                        child2.get(
                                                                                            'lemma')
                                                        # no result yet? --> check index (dependent one)
                                                        if subd7 == "" and not childc and rel_child.find('su') != -1:
                                                            ind_child = childc.get(
                                                                'index')
                                                            # empty
                                                            if not str(ind_child) == "None":
                                                                find_cor_index(
                                                                    ind_child, childb, 7, False)

            ########
            #output#
            ########

            # verb based printing filewriting approach
            # configured for line in file based reading
            if debug == True:
                # filename
                # print("")
                # print(filename)
                i = 1

            # escape csv problems
            sentence = sentence.replace("\n", "")
            context = context.replace("\n", "")

            # None parsers
            if verbd1lemma == "None":
                verbd1lemma = ""

            if verbd2lemma == "None":
                verbd2lemma = ""

            if verbd3lemma == "None":
                verbd3lemma = ""

            if verbd4lemma == "None":
                verbd4lemma = ""

            if verbd5lemma == "None":
                verbd5lemma = ""

            if verbd6lemma == "None":
                verbd6lemma = ""

            if verbd7lemma == "None":
                verbd7lemma = ""

            # Subject none parsers
            if str(subd1) == "None":
                subd1 = ""

            if str(subd2) == "None":
                subd2 = ""

            if str(subd3) == "None":
                subd3 = ""

            if str(subd4) == "None":
                subd4 = ""

            if str(subd5) == "None":
                subd5 = ""

            if str(subd6) == "None":
                subd6 = ""

            if str(subd7) == "None":
                subd7 = ""

            # Object none parsers
            if str(objd1) == "None":
                objd1 = ""

            if str(objd2) == "None":
                objd2 = ""

            if str(objd3) == "None":
                objd3 = ""

            if str(objd4) == "None":
                objd4 = ""

            if str(objd5) == "None":
                objd5 = ""

            if str(objd6) == "None":
                objd6 = ""

            if str(objd7) == "None":
                objd7 = ""

            # subject fixes
            if subd1.find(",") != -1:
                subd1 = subd1.replace(",", "")

            if subd2.find(",") != -1:
                subd2 = subd2.replace(",", "")

            if subd3.find(",") != -1:
                subd3 = subd3.replace(",", "")

            if subd4.find(",") != -1:
                subd4 = subd4.replace(",", "")

            if subd5.find(",") != -1:
                subd5 = subd5.replace(",", "")

            if subd6.find(",") != -1:
                subd6 = subd6.replace(",", "")

            if subd7.find(",") != -1:
                subd7 = subd7.replace(",", "")

            # object fixes
            if objd1.find(",") != -1:
                objd1 = objd1.replace(",", "")

            if objd2.find(",") != -1:
                objd2 = objd2.replace(",", "")

            if objd3.find(",") != -1:
                objd3 = objd3.replace(",", "")

            if objd4.find(",") != -1:
                objd4 = objd4.replace(",", "")

            if objd5.find(",") != -1:
                objd5 = objd5.replace(",", "")

            if objd6.find(",") != -1:
                objd6 = objd6.replace(",", "")

            if objd7.find(",") != -1:
                objd7 = objd7.replace(",", "")

            # subject lemma fixes
            if slemd1.find(",") != -1:
                slemd1 = slemd1.replace(",", "")

            if slemd2.find(",") != -1:
                slemd2 = slemd2.replace(",", "")

            if slemd3.find(",") != -1:
                slemd3 = slemd3.replace(",", "")

            if slemd4.find(",") != -1:
                slemd4 = slemd4.replace(",", "")

            if slemd5.find(",") != -1:
                slemd5 = slemd5.replace(",", "")

            if slemd6.find(",") != -1:
                slemd6 = slemd6.replace(",", "")

            if slemd7.find(",") != -1:
                slemd7 = slemd7.replace(",", "")

            # object lemma fixes
            if olemd1.find(",") != -1:
                olemd1 = olemd1.replace(",", "")

            if olemd2.find(",") != -1:
                olemd2 = olemd2.replace(",", "")

            if olemd3.find(",") != -1:
                olemd3 = olemd3.replace(",", "")

            if olemd4.find(",") != -1:
                olemd4 = olemd4.replace(",", "")

            if olemd5.find(",") != -1:
                olemd5 = olemd5.replace(",", "")

            if olemd6.find(",") != -1:
                olemd6 = olemd6.replace(",", "")

            if olemd7.find(",") != -1:
                olemd7 = olemd7.replace(",", "")

            # ? Now we do the same fixes but for points instead of kommas.

             # subject fixes
            if subd1.find(".") != -1:
                subd1 = subd1.replace(".", "")

            if subd2.find(".") != -1:
                subd2 = subd2.replace(".", "")

            if subd3.find(".") != -1:
                subd3 = subd3.replace(".", "")

            if subd4.find(".") != -1:
                subd4 = subd4.replace(".", "")

            if subd5.find(".") != -1:
                subd5 = subd5.replace(".", "")

            if subd6.find(".") != -1:
                subd6 = subd6.replace(".", "")

            if subd7.find(".") != -1:
                subd7 = subd7.replace(".", "")

            # object fixes
            if objd1.find(".") != -1:
                objd1 = objd1.replace(".", "")

            if objd2.find(".") != -1:
                objd2 = objd2.replace(".", "")

            if objd3.find(".") != -1:
                objd3 = objd3.replace(".", "")

            if objd4.find(".") != -1:
                objd4 = objd4.replace(".", "")

            if objd5.find(".") != -1:
                objd5 = objd5.replace(".", "")

            if objd6.find(".") != -1:
                objd6 = objd6.replace(".", "")

            if objd7.find(".") != -1:
                objd7 = objd7.replace(".", "")

            # subject lemma fixes
            if slemd1.find(".") != -1:
                slemd1 = slemd1.replace(".", "")

            if slemd2.find(".") != -1:
                slemd2 = slemd2.replace(".", "")

            if slemd3.find(".") != -1:
                slemd3 = slemd3.replace(".", "")

            if slemd4.find(".") != -1:
                slemd4 = slemd4.replace(".", "")

            if slemd5.find(".") != -1:
                slemd5 = slemd5.replace(".", "")

            if slemd6.find(".") != -1:
                slemd6 = slemd6.replace(".", "")

            if slemd7.find(".") != -1:
                slemd7 = slemd7.replace(".", "")

            # object lemma fixes
            if olemd1.find(".") != -1:
                olemd1 = olemd1.replace(".", "")

            if olemd2.find(".") != -1:
                olemd2 = olemd2.replace(".", "")

            if olemd3.find(".") != -1:
                olemd3 = olemd3.replace(".", "")

            if olemd4.find(".") != -1:
                olemd4 = olemd4.replace(".", "")

            if olemd5.find(".") != -1:
                olemd5 = olemd5.replace(".", "")

            if olemd6.find(".") != -1:
                olemd6 = olemd6.replace(".", "")

            if olemd7.find(".") != -1:
                olemd7 = olemd7.replace(".", "")

            # sentence fixes
            if sentence.find(",") != -1 or sentence.find(";") != -1:
                sentence = '"' + sentence + '"'

            if sentence[0:1] == " ":
                sentence = sentence[1:]

            # context fixes
            if context.find("  ") != -1:
                context = context.replace("  ", " ")

            # *! ACTUAL OUTPUT

            if verbd1 != "" and verbd1 != " " and verbd1 != "\n":
                # actual output
                word_offset = sentence.rfind(verbd1)
                sen_sta_id = context.find(sentence)
                sen_end_id = sen_sta_id + len(sentence)

                output = "COV_fragment01" + " " + "unknown number" + " " + "0" + " " 
                f.write(output)
            if verbd2 != "" and verbd2 != " " and verbd2 != "\n":
                # actual output
                word_offset = sentence.rfind(verbd2)
                sen_sta_id = context.find(sentence)
                sen_end_id = sen_sta_id + len(sentence)

                output = "COV,1,1,news," + "COV_fragment01_" + str(filenumber) + "_0," + '"' + context + '"' + ",test," + str(
                    sen_end_id) + "," + str(sentence_number) + ",0," + str(sen_sta_id) + ",0" + ",COV-fragment01," + verbd2 + ","
                output = output + str(word_offset) + "," + str(subd2) + "," + str(
                    objd2) + "," + slemd2 + "," + olemd2 + "," + verbd2lemma + "," + sentence + ",0," + "\n"
                f.write(output)
            if verbd3 != "" and verbd3 != " " and verbd3 != "\n":
                # actual output
                word_offset = sentence.rfind(verbd3)
                sen_sta_id = context.find(sentence)
                sen_end_id = sen_sta_id + len(sentence)

                output = "COV,1,1,news," + "COV_fragment01_" + str(filenumber) + "_0," + '"' + context + '"' + ",test," + str(
                    sen_end_id) + "," + str(sentence_number) + ",0," + str(sen_sta_id) + ",0" + ",COV-fragment01," + verbd3 + ","
                output = output + str(word_offset) + "," + str(subd3) + "," + str(
                    objd3) + "," + slemd3 + "," + olemd3 + "," + verbd3lemma + "," + sentence + ",0," + "\n"
                f.write(output)
            if verbd4 != "" and verbd4 != " " and verbd4 != "\n":
                # actual output
                word_offset = sentence.rfind(verbd4)
                sen_sta_id = context.find(sentence)
                sen_end_id = sen_sta_id + len(sentence)

                output = "COV,1,1,news," + "COV_fragment01_" + str(filenumber) + "_0," + '"' + context + '"' + ",test," + str(
                    sen_end_id) + "," + str(sentence_number) + ",0," + str(sen_sta_id) + ",0" + ",COV-fragment01," + verbd4 + ","
                output = output + str(word_offset) + "," + str(subd4) + "," + str(
                    objd4) + "," + slemd4 + "," + olemd4 + "," + verbd4lemma + "," + sentence + ",0," + "\n"
                f.write(output)
            if verbd5 != "" and verbd5 != " " and verbd5 != "\n":
                # actual output
                word_offset = sentence.rfind(verbd5)
                sen_sta_id = context.find(sentence)
                sen_end_id = sen_sta_id + len(sentence)

                output = "COV,1,1,news," + "COV_fragment01_" + str(filenumber) + "_0," + '"' + context + '"' + ",test," + str(
                    sen_end_id) + "," + str(sentence_number) + ",0," + str(sen_sta_id) + ",0" + ",COV-fragment01," + verbd5 + ","
                output = output + str(word_offset) + "," + str(subd5) + "," + str(
                    objd5) + "," + slemd5 + "," + olemd5 + "," + verbd5lemma + "," + sentence + ",0," + "\n"
                f.write(output)
            if verbd6 != "" and verbd6 != " " and verbd6 != "\n":
                # actual output
                word_offset = sentence.rfind(verbd6)
                sen_sta_id = context.find(sentence)
                sen_end_id = sen_sta_id + len(sentence)

                output = "COV,1,1,news," + "COV_fragment01_" + str(filenumber) + "_0," + '"' + context + '"' + ",test," + str(
                    sen_end_id) + "," + str(sentence_number) + ",0," + str(sen_sta_id) + ",0" + ",COV-fragment01," + verbd6 + ","
                output = output + str(word_offset) + "," + str(subd6) + "," + str(
                    objd6) + "," + slemd6 + "," + olemd6 + "," + verbd6lemma + "," + sentence + ",0," + "\n"
                f.write(output)
            if verbd7 != "" and verbd7 != " " and verbd7 != "\n":
                # actual output
                word_offset = sentence.rfind(verbd7)
                sen_sta_id = context.find(sentence)
                sen_end_id = sen_sta_id + len(sentence)

                output = "COV,1,1,news," + "COV_fragment01_" + str(filenumber) + "_0," + '"' + context + '"' + ",test," + str(
                    sen_end_id) + "," + str(sentence_number) + ",0," + str(sen_sta_id) + ",0" + ",COV-fragment01," + verbd7 + ","
                output = output + str(word_offset) + "," + str(subd7) + "," + str(
                    objd7) + "," + slemd7 + "," + olemd7 + "," + verbd7lemma + "," + sentence + ",0," + "\n"
                f.write(output)

    f.close()