#########################################################################
#PROGRAM NAME: Metadata Seperator                                       #
#PROGRAM AUTHOR: Joost Grunwald                                         # 
#PROGRAM PURPOSE: seperation of NEXISUNI metadata from a .txt nexisbatch#
#PROGRAM PURPOSE: It also gathers general metadata of the full set      #
#########################################################################

##############
#dependencies#
##############
import os

##########
#SETTINGS#
##########

#input directory (input form = .txt inclusive metadata)
directory = r"C:\Users\joost\Documents\work\radboud\dataset_txt_renamed"

#output_directory (output form = .txt exclusive metadata + seperate metadata)
directory_out = r"C:\Users\joost\Documents\work\radboud\dataset_txt_meta"

#If true this uses the title (needs renamer.py) for fetching certain metadata
#If False this tries to use the inner file content instead
titlemode = True

#counter used to count amount of files in database
filecounter = 0

############
#UI SERVICE#
############
print(" _______  _______ _________ _______  ______   _______ _________ _______    _______          _________ _______  _______  _______ _________ _______  _______ ")
print("(       )(  ____ \\__   __/(  ___  )(  __  \ (  ___  )\__   __/(  ___  )  (  ____ \|\     /|\__   __/(  ____ )(  ___  )(  ____ \\__   __/(  ___  )(  ____ )")
print("| () () || (    \/   ) (   | (   ) || (  \  )| (   ) |   ) (   | (   ) |  | (    \/( \   / )   ) (   | (    )|| (   ) || (    \/   ) (   | (   ) || (    )|")
print("| || || || (__       | |   | (___) || |   ) || (___) |   | |   | (___) |  | (__     \ (_) /    | |   | (____)|| (___) || |         | |   | |   | || (____)|")
print("| |(_)| ||  __)      | |   |  ___  || |   | ||  ___  |   | |   |  ___  |  |  __)     ) _ (     | |   |     __)|  ___  || |         | |   | |   | ||     __)")
print("| |   | || (         | |   | (   ) || |   ) || (   ) |   | |   | (   ) |  | (       / ( ) \    | |   | (\ (   | (   ) || |         | |   | |   | || (\ (   ")
print("| )   ( || (____/\   | |   | )   ( || (__/  )| )   ( |   | |   | )   ( |  | (____/\( /   \ )   | |   | ) \ \__| )   ( || (____/\   | |   | (___) || ) \ \__")
print("|/     \|(_______/   )_(   |/     \|(______/ |/     \|   )_(   |/     \|  (_______/|/     \|   )_(   |/   \__/|/     \|(_______/   )_(   (_______)|/   \__/")
print("")
print("")
print("This program extracts metadata from NexisUni .txt batches")
print("meta_extractor.titlemode = " + str(titlemode))

###########
#FUNCTIONS#
###########
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

###############
#global values#
###############

#for general metadata analysis of a dataset per source
ad_articles = 0
nrc_articles = 0
teleg_articles = 0
trouw_articles = 0
volks_articles = 0
     
#for general metadata analysis of a dataset per month
mo_1_articles = 0
mo_2_articles = 0
mo_3_articles = 0
mo_4_articles = 0
mo_5_articles = 0
mo_6_articles = 0
mo_7_articles = 0
mo_8_articles = 0
mo_9_articles = 0
mo_10_articles = 0
mo_11_articles = 0
mo_12_articles = 0

#for source specific metadata analysis of a dataeset per month
mo_1_ad_articles = 0
mo_1_nrc_articles = 0
mo_1_teleg_articles = 0
mo_1_trouw_articles = 0
mo_1_volks_articles = 0

mo_2_ad_articles = 0
mo_2_nrc_articles = 0
mo_2_teleg_articles = 0
mo_2_trouw_articles = 0
mo_2_volks_articles = 0

mo_3_ad_articles = 0
mo_3_nrc_articles = 0
mo_3_teleg_articles = 0
mo_3_trouw_articles = 0
mo_3_volks_articles = 0

mo_4_ad_articles = 0
mo_4_nrc_articles = 0
mo_4_teleg_articles = 0
mo_4_trouw_articles = 0
mo_4_volks_articles = 0

mo_5_ad_articles = 0
mo_5_nrc_articles = 0
mo_5_teleg_articles = 0
mo_5_trouw_articles = 0
mo_5_volks_articles = 0

mo_6_ad_articles = 0
mo_6_nrc_articles = 0
mo_6_teleg_articles = 0
mo_6_trouw_articles = 0
mo_6_volks_articles = 0

mo_7_ad_articles = 0
mo_7_nrc_articles = 0
mo_7_teleg_articles = 0
mo_7_trouw_articles = 0
mo_7_volks_articles = 0

mo_8_ad_articles = 0
mo_8_nrc_articles = 0
mo_8_teleg_articles = 0
mo_8_trouw_articles = 0
mo_8_volks_articles = 0

mo_9_ad_articles = 0
mo_9_nrc_articles = 0
mo_9_teleg_articles = 0
mo_9_trouw_articles = 0
mo_9_volks_articles = 0

mo_10_ad_articles = 0
mo_10_nrc_articles = 0
mo_10_teleg_articles = 0
mo_10_trouw_articles = 0
mo_10_volks_articles = 0

mo_11_ad_articles = 0
mo_11_nrc_articles = 0
mo_11_teleg_articles = 0
mo_11_trouw_articles = 0
mo_11_volks_articles = 0

mo_12_ad_articles = 0
mo_12_nrc_articles = 0
mo_12_teleg_articles = 0
mo_12_trouw_articles = 0
mo_12_volks_articles = 0
     
################
#CODE ITERATION#
################

#for every file in the input_directory
for file in os.listdir(directory):

     #the filename is decoded from the file
     filename = os.fsdecode(file)

     #we init some spile specific variables
     source = ""
     article_kind = 0

     #for every file in input_directory with .txt extension
     
     if filename.endswith(".txt"):
         #increment the filecounter
         filecounter += 1
         
         ################
         #TITLE ANALYSIS#
         ################

         #if setting partially extract using title is enabled
         if titlemode == True:
              
              #we first try to find the AD title
              source_ad = filename.find("AD")
              if source_ad != -1:
                  #if source found we process it accordingly
                  source = "Algemeen Dagblad"
                  ad_articles = ad_articles + 1
                  article_kind = 1
              else:
                  #if not AD we try NRC
                  source_nrc = filename.find("NRC")
                  if source_nrc != -1:
                      #if source found we process it accordingly
                      source = "Nrc Handelsblad"
                      nrc_articles = nrc_articles + 1
                      article_kind = 2
                  else:
                      #if not NRC we try Telegraaf
                      source_telegraaf = filename.find("TELEGRAAF")
                      if source_telegraaf != -1:
                         #if source found we process it accordingly
                          source = "Telegraaf"
                          teleg_articles = teleg_articles + 1
                          article_kind = 3
                      else:
                          #if not Telegraaf we will try Trouw
                          source_trouw = filename.find("TROUW")
                          if source_trouw != -1:
                              #if source found we process it accordingly
                              source = "Trouw"
                              trouw_articles = trouw_articles + 1
                              article_kind = 4
                          else:
                              #if not Trouw we will try Volkskrant
                              source_volkskrant = filename.find("VOLKSKRANT")
                              if source_volkskrant != -1:
                                  #if source found we process it accordingly
                                  source = "volkskrant"
                                  volks_articles = volks_articles + 1
                                  article_kind = 5
                                  
         ###################################
         #gather general metadata of months#
         ###################################

         #Future version --> a function of this would be much more structured

         #month based iteration using Capital and not capital variant (as both are used by different sources)                                  
         month = filename.find("januari")
         if month == -1:
              month = filename.find("Januari")
         if month != -1:
              #based on month increment right counter
              mo_1_articles = mo_1_articles + 1
              if article_kind == 1:
                   mo_1_ad_articles = mo_1_ad_articles + 1
              elif article_kind == 2:
                   mo_1_nrc_articles = mo_1_nrc_articles + 1
              elif article_kind == 3:
                   mo_1_teleg_articles = mo_1_teleg_articles + 1
              elif article_kind == 4:
                   mo_1_trouw_articles = mo_1_trouw_articles + 1
              elif article_kind == 5:
                   mo_1_volks_articles = mo_1_volks_articles + 1

         month = filename.find("februari")
         if month == -1:
              month = filename.find("Februari")
         if month != -1:
              mo_2_articles = mo_2_articles + 1
              if article_kind == 1:
                   mo_2_ad_articles = mo_2_ad_articles + 1
              elif article_kind == 2:
                   mo_2_nrc_articles = mo_2_nrc_articles + 1
              elif article_kind == 3:
                   mo_2_teleg_articles = mo_2_teleg_articles + 1
              elif article_kind == 4:
                   mo_2_trouw_articles = mo_2_trouw_articles + 1
              elif article_kind == 5:
                   mo_2_volks_articles = mo_2_volks_articles + 1

         month = filename.find("maart")
         if month == -1:
              month = filename.find("Maart")
         if month != -1:
              mo_3_articles = mo_3_articles + 1
              if article_kind == 1:
                   mo_3_ad_articles = mo_3_ad_articles + 1
              elif article_kind == 2:
                   mo_3_nrc_articles = mo_3_nrc_articles + 1
              elif article_kind == 3:
                   mo_3_teleg_articles = mo_3_teleg_articles + 1
              elif article_kind == 4:
                   mo_3_trouw_articles = mo_3_trouw_articles + 1
              elif article_kind == 5:
                   mo_3_volks_articles = mo_3_volks_articles + 1

         month = filename.find("april")
         if month == -1:
              month = filename.find("April")
         if month != -1:
              mo_4_articles = mo_4_articles + 1
              if article_kind == 1:
                   mo_4_ad_articles = mo_4_ad_articles + 1
              elif article_kind == 2:
                   mo_4_nrc_articles = mo_4_nrc_articles + 1
              elif article_kind == 3:
                   mo_4_teleg_articles = mo_4_teleg_articles + 1
              elif article_kind == 4:
                   mo_4_trouw_articles = mo_4_trouw_articles + 1
              elif article_kind == 5:
                   mo_4_volks_articles = mo_4_volks_articles + 1

         month = filename.find("mei")
         if month == -1:
              month = filename.find("Mei")
         if month != -1:
              mo_5_articles = mo_5_articles + 1
              if article_kind == 1:
                   mo_5_ad_articles = mo_5_ad_articles + 1
              elif article_kind == 2:
                   mo_5_nrc_articles = mo_5_nrc_articles + 1
              elif article_kind == 3:
                   mo_5_teleg_articles = mo_5_teleg_articles + 1
              elif article_kind == 4:
                   mo_5_trouw_articles = mo_5_trouw_articles + 1
              elif article_kind == 5:
                   mo_5_volks_articles = mo_5_volks_articles + 1

         month = filename.find("juni")
         if month == -1:
              month = filename.find("Juni")
         if month != -1:
              mo_6_articles = mo_6_articles + 1
              if article_kind == 1:
                   mo_6_ad_articles = mo_6_ad_articles + 1
              elif article_kind == 2:
                   mo_6_nrc_articles = mo_6_nrc_articles + 1
              elif article_kind == 3:
                   mo_6_teleg_articles = mo_6_teleg_articles + 1
              elif article_kind == 4:
                   mo_6_trouw_articles = mo_6_trouw_articles + 1
              elif article_kind == 5:
                   mo_6_volks_articles = mo_6_volks_articles + 1

         month = filename.find("juli")
         if month == -1:
              month = filename.find("Juli")
         if month != -1:
              mo_7_articles = mo_7_articles + 1
              if article_kind == 1:
                   mo_7_ad_articles = mo_7_ad_articles + 1
              elif article_kind == 2:
                   mo_7_nrc_articles = mo_7_nrc_articles + 1
              elif article_kind == 3:
                   mo_7_teleg_articles = mo_7_teleg_articles + 1
              elif article_kind == 4:
                   mo_7_trouw_articles = mo_7_trouw_articles + 1
              elif article_kind == 5:
                   mo_7_volks_articles = mo_7_volks_articles + 1

         month = filename.find("augustus")
         if month == -1:
              month = filename.find("Augustus")
         if month != -1:
              mo_8_articles = mo_8_articles + 1
              if article_kind == 1:
                   mo_8_ad_articles = mo_8_ad_articles + 1
              elif article_kind == 2:
                   mo_8_nrc_articles = mo_8_nrc_articles + 1
              elif article_kind == 3:
                   mo_8_teleg_articles = mo_8_teleg_articles + 1
              elif article_kind == 4:
                   mo_8_trouw_articles = mo_8_trouw_articles + 1
              elif article_kind == 5:
                   mo_8_volks_articles = mo_8_volks_articles + 1

         month = filename.find("september")
         if month == -1:
              month = filename.find("September")
         if month != -1:
              mo_9_articles = mo_9_articles + 1
              if article_kind == 1:
                   mo_9_ad_articles = mo_9_ad_articles + 1
              elif article_kind == 2:
                   mo_9_nrc_articles = mo_9_nrc_articles + 1
              elif article_kind == 3:
                   mo_9_teleg_articles = mo_9_teleg_articles + 1
              elif article_kind == 4:
                   mo_9_trouw_articles = mo_9_trouw_articles + 1
              elif article_kind == 5:
                   mo_9_volks_articles = mo_9_volks_articles + 1

         month = filename.find("oktober")
         if month == -1:
              month = filename.find("Oktober")
         if month != -1:
              mo_10_articles = mo_10_articles + 1
              if article_kind == 1:
                   mo_10_ad_articles = mo_10_ad_articles + 1
              elif article_kind == 2:
                   mo_10_nrc_articles = mo_10_nrc_articles + 1
              elif article_kind == 3:
                   mo_10_teleg_articles = mo_10_teleg_articles + 1
              elif article_kind == 4:
                   mo_10_trouw_articles = mo_10_trouw_articles + 1
              elif article_kind == 5:
                   mo_10_volks_articles = mo_10_volks_articles + 1

         month = filename.find("november")
         if month == -1:
              month = filename.find("November")
         if month != -1:
              mo_11_articles = mo_11_articles + 1
              if article_kind == 1:
                   mo_11_ad_articles = mo_11_ad_articles + 1
              elif article_kind == 2:
                   mo_11_nrc_articles = mo_11_nrc_articles + 1
              elif article_kind == 3:
                   mo_11_teleg_articles = mo_11_teleg_articles + 1
              elif article_kind == 4:
                   mo_11_trouw_articles = mo_11_trouw_articles + 1
              elif article_kind == 5:
                   mo_11_volks_articles = mo_11_volks_articles + 1

         month = filename.find("december")
         if month == -1:
              month = filename.find("December")
         if month != -1:
              mo_12_articles = mo_12_articles + 1
              if article_kind == 1:
                   mo_12_ad_articles = mo_12_ad_articles + 1
              elif article_kind == 2:
                   mo_12_nrc_articles = mo_12_nrc_articles + 1
              elif article_kind == 3:
                   mo_12_teleg_articles = mo_12_teleg_articles + 1
              elif article_kind == 4:
                   mo_12_trouw_articles = mo_12_trouw_articles + 1
              elif article_kind == 5:
                   mo_12_volks_articles = mo_12_volks_articles + 1

         #########################
         #META BLOCK ONE ANALYSIS#
         #########################

         #we define our metadata values
         title = ""
         date = ""
         section = ""
         length = ""
         byline = ""
         dateline = ""
         highlight = ""
         graphics = 0
         load_date = ""
         
         with open(directory + "\\" + filename, encoding="utf8") as fp:
           line = fp.readline()
           cnt = 1

           #we define our exit conditions
           sourcereached = False
           datereached = False
           linereached = False
           lengthreached = False
           bylinereached = False
           datelinereached = False
           highlightreached = False
           loaddatereached = False

           fulltext = ""
           while line:
               if line == "":
                   continue

               #now we will get the current source
               #IMPORTANT: if you use other sources, make sure to insert their title in this code block
               elif titlemode == False and sourcereached == False:
                    if line.find("Algemeen Dagblad") != -1:
                         sourcereached = True
                         source = line
                         ad_articles = ad_articles + 1
                         continue
                    elif line.find("NRC Handelsblad") != -1:
                         sourcereached = True
                         source = line
                         nrc_articles = nrc_articles + 1
                         continue
                    elif line.find("De Telegraaf") != -1:
                         sourcereached = True
                         source = line
                         teleg_articles = teleg_articles + 1
                         continue
                    elif line.find("Trouw") != -1:
                         sourcereached = True
                         source = line
                         trouw_articles = trouw_articles + 1
                         continue
                    elif line.find("de Volkskrant") != -1:
                         sourcereached = True
                         source = line
                         volks_articles = volks_articles + 1
                         continue

               #now we will get the current date
               elif line.find("2020") != -1 and datereached == False: #for now this only works for 2020, this has to be edited in the future.
                   datereached = True
                   date = line
                   continue
   
               #now we will get the section
               elif line.find("Section:") != -1 and linereached == False:
                   linereached = True
                   section = line
                   continue

               #now we will get the length
               elif line.find("Length:") != -1 and lengthreached == False:
                   lengthreached = True
                   length = line
                   continue

               #now we will get the byline --> this mostly contains author information
               elif line.find("Byline:") != -1 and bylinereached == False:
                   bylinereached = True
                   byline = line
                   continue

               #now we will get the dateline --> this mostly contains location information
               elif line.find("Dateline:") != -1 and datelinereached == False:
                   datelinereached = True
                   dateline = line
                   continue

               #now we will get the highlight
               elif line.find("Highlight:") != -1 and highlightreached == False:
                   highlightreached = True
                   highlight = line
                   continue

               #now we will count the amount of images present
               elif line.find("Graphic") != -1:
                    graphics = graphics + 1
                    cnt += 1
                    line = fp.readline()
                    continue

               #last we will get the load date from nexisuni batch
               elif line.find("Load-Date:") != -1 and loaddatereached == False:
                    loaddatereached = True
                    loaddate = line
                    continue                 

               fulltext = fulltext + line
               
               cnt += 1

               line = fp.readline()

         fp.close()

         start_index_title = find_nth(fulltext, "\n", 1)
         end_index_title = find_nth(fulltext, "\n", 2)
         title = fulltext[start_index_title+1:end_index_title]

         #remove cases where fulltext is title
         if title.find("....") != -1:
              title = "Titel onbekend"

         #clear fulltext
         if fulltext.find("Body") != -1:
              textstart = fulltext.index("Body")
              textstart = textstart + 4 #include the 4 characters
              
              #lets try to find ending pieces
              if fulltext.find("Bekijk de oorspronkelijke pagina:") != -1:
                  index_oorsp = fulltext.index("Bekijk de oorspronkelijke pagina:")
              else:
                  index_oorsp = -1 #not found
                  
              if fulltext.find("Load-Date:") != -1 :         
                  index_load_date = fulltext.index("Load-Date:")
              else:
                  index_load_date = -1

              if fulltext.find("End of Document") != -1:    
                  index_end_doc = fulltext.index("End of Document")
              else:
                  index_end_doc = -1
              
              final_index = index_oorsp
              if  final_index == -1:
                  final_index = index_load_date
              if  final_index == -1:
                  final_index = index_end_doc
                  
              if index_load_date < final_index and index_load_date != -1:
                  final_index = index_load_date
              if index_end_doc < final_index and index_end_doc != -1:
                  final_index = index_end_doc

              if final_index == -1:
                  fulltext = fulltext[textstart:]
              else:
                  fulltext = fulltext[textstart:final_index]
                  
              #replace graphic
              if graphics != 0:
                   fulltext.replace("Graphic","")
              
              #now we will overwrite our current files
              f = open(directory_out + "\\" + filename, "w", encoding="utf8")
              f.write(fulltext)
              f.close()

              #now we will create metadata files
              filename_meta = filename.replace(".txt","")
              filename_meta = filename_meta + "_meta.txt"
              f = open(directory_out + "\\" + filename_meta, "w", encoding="utf8")
              counter = 0

              #title
              if title != "":
                   f.write(str(counter) + " Titel: " + str(title))
              counter = counter + 1
              
              #source
              if source != "":
                   if source.find("\n") == -1:
                        source = source + "\n"
                   f.write(str(counter) + " Bron: " + source)
              else:
                   f.write(str(counter) + " Bron: Onbekend" + "\n")
              counter = counter + 1

              #date
              if date != "":
                   if date.find("\n") == -1:
                        date = date + "\n"
                   f.write(str(counter) + " Datum: " + date)
              else:
                   f.write(str(counter) + " Datum: Onbekend" + "\n")
              counter = counter + 1

              #section
              if section != "":
                   if section.find("\n") == -1:
                        section = section + "\n"
                   f.write(str(counter) + " " + section)
              else:
                   f.write(str(counter) + " Sectie: Onbekend" + "\n")
              counter = counter + 1

              #length
              if length != "":
                   if length.find("\n") == -1:
                        length = length + "\n"
                   f.write(str(counter) + " " + length)
              else:
                   f.write(str(counter) + " Lengte: Onbekend" + "\n")
              counter = counter + 1

              #byline
              if byline != "":
                   if byline.find("\n") == -1:
                        byline = byline + "\n"
                   f.write(str(counter) + " " + byline)
              else:
                   f.write(str(counter) + " Auteur: Onbekend" + "\n")
              counter = counter + 1

              #dateline
              if dateline != "":
                    if dateline.find("\n") == -1:
                        dateline = dateline + "\n"
                    f.write(str(counter) + " " + dateline)
              else:
                    f.write(str(counter) + " Locatie: Onbekend" + "\n")
              counter = counter + 1

              #highlight
              if highlight != "":
                   if highlight.find("\n") == -1:
                        hightlight = highlight + "\n"
                   f.write(str(counter) + " " + highlight)
              else:
                   f.write(str(counter) + " Highlight: Onbekend" + "\n")
              counter = counter + 1

              #graphics
              f.write(str(counter) + " Aantal foto's: " + str(graphics) + "\n")
              counter = counter + 1

              #loaddate
              if loaddate != "":
                   f.write(str(counter) + " " + loaddate)
              else:
                   f.write(str(counter) + " Datum van laden: Onbekend")
                   
              f.close()

              if filecounter == 35000 or filecounter == 40000 or filecounter == 1000 or filecounter == 2500 or filecounter == 5000 or filecounter == 7500 or filecounter == 10000 or filecounter == 12500 or filecounter == 15000 or filecounter == 17500 or filecounter == 20000 or filecounter == 25000 or filecounter == 30000:
                   print("Amount of files parsed: " + str(filecounter))
          
              continue
         else:
              print("Body not found at: " + str(filecounter) + " filename: "  + str(filename))
              continue

         #get full data and remove lines
     else:
         continue

print("")
print("All metadata seperated")
print("All raw text saved")

#general metadata
f = open(directory_out + "\\1-general_metadata.txt", "w", encoding="utf8")
totalarticles = ad_articles + nrc_articles + teleg_articles + volks_articles + trouw_articles
f.write(" /$$      /$$             /$$                     /$$             /$$               \n")
f.write(" | $$$    /$$$            | $$                    | $$            | $$              \n") 
f.write(" | $$$$  /$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$ \n")
f.write(" | $$ $$/$$ $$ /$$__  $$|_  $$_/   |____  $$ /$$__  $$ |____  $$|_  $$_/   |____  $$\n")
f.write(" | $$  $$$| $$| $$$$$$$$  | $$      /$$$$$$$| $$  | $$  /$$$$$$$  | $$      /$$$$$$$\n")
f.write(" | $$\  $ | $$| $$_____/  | $$ /$$ /$$__  $$| $$  | $$ /$$__  $$  | $$ /$$ /$$__  $$\n")
f.write(" | $$ \/  | $$|  $$$$$$$  |  $$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$$\n")
f.write(" |__/     |__/ \_______/   \___/   \_______/ \_______/ \_______/   \___/   \_______/\n")
f.write("")
f.write("Total amount of articles in database: " + str(totalarticles) + "\n")
f.write("\n")
f.write("ARTICLES ORDERED BY SOURCE\n")
f.write("AD Articles: " + str(ad_articles) + "\n")
f.write("NRC Articles: " + str(nrc_articles) + "\n")
f.write("Telegraaf Articles: " + str(teleg_articles) + "\n")
f.write("Volkskrant Articles: " + str(volks_articles) + "\n")
f.write("Trouw Articles: " + str(trouw_articles) + "\n")
f.write("\n")
f.write("ARTICLES ORDERED BY MONTH\n")
f.write("January Articles: " + str(mo_1_articles) + "\n")
f.write("February Articles: " + str(mo_2_articles) + "\n")
f.write("March Articles: " + str(mo_3_articles) + "\n")
f.write("Avril Articles: " + str(mo_4_articles) + "\n")
f.write("May Articles: " + str(mo_5_articles) + "\n")
f.write("June Articles: " + str(mo_6_articles) + "\n")
f.write("July Articles: " + str(mo_7_articles) + "\n")
f.write("August Articles: " + str(mo_8_articles) + "\n")
f.write("September Articles: " + str(mo_9_articles) + "\n")     
f.write("October Articles: " + str(mo_10_articles) + "\n")
f.write("November Articles: " + str(mo_11_articles) + "\n")
f.write("December Articles: " + str(mo_12_articles) + "\n")
f.write("\n")
f.write("ARTICLES ORDERED BY MONTH * SOURCE\n")
f.write("\n")
f.write("ALGEMEEN DAGBLAD\n")
f.write("January Articles: " + str(mo_1_ad_articles) + "\n")
f.write("February Articles: " + str(mo_2_ad_articles) + "\n")
f.write("March Articles: " + str(mo_3_ad_articles) + "\n")
f.write("Avril Articles: " + str(mo_4_ad_articles) + "\n")
f.write("May Articles: " + str(mo_5_ad_articles) + "\n")
f.write("June Articles: " + str(mo_6_ad_articles) + "\n")
f.write("July Articles: " + str(mo_7_ad_articles) + "\n")
f.write("August Articles: " + str(mo_8_ad_articles) + "\n")
f.write("September Articles: " + str(mo_9_ad_articles) + "\n")     
f.write("October Articles: " + str(mo_10_ad_articles) + "\n")
f.write("November Articles: " + str(mo_11_ad_articles) + "\n")
f.write("December Articles: " + str(mo_12_ad_articles) + "\n")
f.write("\n")
f.write("NRC HANDELSBLAD\n")
f.write("January Articles: " + str(mo_1_nrc_articles) + "\n")
f.write("February Articles: " + str(mo_2_nrc_articles) + "\n")
f.write("March Articles: " + str(mo_3_nrc_articles) + "\n")
f.write("Avril Articles: " + str(mo_4_nrc_articles) + "\n")
f.write("May Articles: " + str(mo_5_nrc_articles) + "\n")
f.write("June Articles: " + str(mo_6_nrc_articles) + "\n")
f.write("July Articles: " + str(mo_7_nrc_articles) + "\n")
f.write("August Articles: " + str(mo_8_nrc_articles) + "\n")
f.write("September Articles: " + str(mo_9_nrc_articles) + "\n")     
f.write("October Articles: " + str(mo_10_nrc_articles) + "\n")
f.write("November Articles: " + str(mo_11_nrc_articles) + "\n")
f.write("December Articles: " + str(mo_12_nrc_articles) + "\n")
f.write("\n")
f.write("TELEGRAAF\n")
f.write("January Articles: " + str(mo_1_teleg_articles) + "\n")
f.write("February Articles: " + str(mo_2_teleg_articles) + "\n")
f.write("March Articles: " + str(mo_3_teleg_articles) + "\n")
f.write("Avril Articles: " + str(mo_4_teleg_articles) + "\n")
f.write("May Articles: " + str(mo_5_teleg_articles) + "\n")
f.write("June Articles: " + str(mo_6_teleg_articles) + "\n")
f.write("July Articles: " + str(mo_7_teleg_articles) + "\n")
f.write("August Articles: " + str(mo_8_teleg_articles) + "\n")
f.write("September Articles: " + str(mo_9_teleg_articles) + "\n")     
f.write("October Articles: " + str(mo_10_teleg_articles) + "\n")
f.write("November Articles: " + str(mo_11_teleg_articles) + "\n")
f.write("December Articles: " + str(mo_12_teleg_articles) + "\n")
f.write("\n")
f.write("TROUW\n")
f.write("January Articles: " + str(mo_1_trouw_articles) + "\n")
f.write("February Articles: " + str(mo_2_trouw_articles) + "\n")
f.write("March Articles: " + str(mo_3_trouw_articles) + "\n")
f.write("Avril Articles: " + str(mo_4_trouw_articles) + "\n")
f.write("May Articles: " + str(mo_5_trouw_articles) + "\n")
f.write("June Articles: " + str(mo_6_trouw_articles) + "\n")
f.write("July Articles: " + str(mo_7_trouw_articles) + "\n")
f.write("August Articles: " + str(mo_8_trouw_articles) + "\n")
f.write("September Articles: " + str(mo_9_trouw_articles) + "\n")     
f.write("October Articles: " + str(mo_10_trouw_articles) + "\n")
f.write("November Articles: " + str(mo_11_trouw_articles) + "\n")
f.write("December Articles: " + str(mo_12_trouw_articles) + "\n")
f.write("\n")
f.write("VOLKSKRANT\n")
f.write("January Articles: " + str(mo_1_volks_articles) + "\n")
f.write("February Articles: " + str(mo_2_volks_articles) + "\n")
f.write("March Articles: " + str(mo_3_volks_articles) + "\n")
f.write("Avril Articles: " + str(mo_4_volks_articles) + "\n")
f.write("May Articles: " + str(mo_5_volks_articles) + "\n")
f.write("June Articles: " + str(mo_6_volks_articles) + "\n")
f.write("July Articles: " + str(mo_7_volks_articles) + "\n")
f.write("August Articles: " + str(mo_8_volks_articles) + "\n")
f.write("September Articles: " + str(mo_9_volks_articles) + "\n")     
f.write("October Articles: " + str(mo_10_volks_articles) + "\n")
f.write("November Articles: " + str(mo_11_volks_articles) + "\n")
f.write("December Articles: " + str(mo_12_volks_articles) + "\n")
f.close()

print("General metadata seperated")

