# Filename: generate_votes.py
# Author: Liu Yunzhu
# Description: Generate VOTES.DAT which is a suitable delimited file of votes,
# with realistic distribution of valid and invalide votes. 

#Assumpitons:
# PAP 52%, WP 40%, SDA 3%, RP 5%
# total votes: 34000 with 98% of valid votes(33300)

import random

def generate():
    # generate 34000 votes
    n = 1
    for n in range (1,34001):
        #proportion of votes for each party
        a = random.randint(1,100)
        party = ""
        if a < 6:
            party = "RP"
        elif a >5 and a < 9:
            party = "SDA"
        elif a > 8 and a < 49:
            party = "WP"
        else:
            party = "PAP"
            
        #proportion of valid votes
        b = random.randint(1,100)
        vote = ""
        if b < 99:
            #valid vote
            vote = ",1"
        else:
            vote = ","

        print (party+vote)
        outfile.write(party+vote + "\n")

        n = n+1
try:
    outfile = open("VOTES.DAT","w")

    generate()

    outfile.close()
except IOError:
    print("cannot write to VOTES.DAT")


