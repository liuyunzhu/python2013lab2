# Filename: count_votes.py
# Author: Liu Yunzhu
# Description: count number and percentage of votes by each party

votes =[]
invalid = 0
pap_votes  = 0
wp_votes = 0
sda_votes = 0
rp_votes = 0

try:
    infile = open("VOTES.DAT","r")

    lines = infile.readlines()
    for line in lines:
        line = line.rstrip()
        votes.append(line)
    total_votes=len(votes)
    print ("total votes: "+str(total_votes))

    # count invalid votes
    for vote in votes:
        if vote[-2] != "," or vote[-1] != "1":
            invalid = invalid +1
            votes.remove(vote)

    print ("invalid votes: "+str(invalid))
    print("total valid votes:" + str(len(votes)))

    #count votes
    for vote in votes:
        if (vote[0:3]) =="PAP":
            pap_votes = pap_votes + 1
        elif (vote[0:3]) =="SDA":
            sda_votes = sda_votes + 1
        elif (vote[0:2]) =="RP":
            rp_votes = rp_votes + 1
        elif (vote[0:2]) =="WP":
            wp_votes = wp_votes + 1

    #calculate percentage
    pap_percent = "{0:0.1f}".format(pap_votes / len(votes) * 100)
    wp_percent = "{0:0.1f}".format(wp_votes / len(votes) * 100)
    rp_percent = "{0:0.1f}".format(rp_votes / len(votes) * 100)
    sda_percent = "{0:0.1f}".format(sda_votes / len(votes) * 100)
    
    #output
    print ("PAP votes: "+ str(pap_votes) +"    Percentage: " + str(pap_percent) + "%")
    print ("WP votes: "+ str(wp_votes)+"    Percentage: " + str(wp_percent) + "%")
    print ("SDA votes: "+ str(sda_votes)+"    Percentage: " + str(sda_percent) + "%")
    print ("RP votes: "+ str(rp_votes)+"    Percentage: " + str(rp_percent) + "%")

    infile.close()
except IOError:
    print("cannot read from VOTES.DAT")
