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

IDEE ACHTER HET ALGORITME
coronawoord in titel --> 6 punten
coronawoord in omslag --> 3 punten
coronawoord --> 1 punt
bevatten eerste vijf zinnen een coronawoord --> dubbele punten
dubbele coronawoorden --> dubbele punten
"""


