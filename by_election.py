# Filename: by_election.py
# Author: Liu Yunzhu
# Description: display election results and output to RESULTS.DAT

#time and date display
import datetime
date = str(datetime.datetime.now().strftime('%d/%m/%Y'))
time = str(datetime.datetime.now().strftime('%H:%M %p'))

#variable and lists
votes =[]
invalid = 0
pap_votes  = 0
wp_votes = 0
sda_votes = 0
rp_votes = 0

try:
    infile = open("VOTES.DAT","r")
    outfile = open("RESULTS.DAT","w")

    #count votes and percentage
    lines = infile.readlines()
    for line in lines:
        line = line.rstrip()
        votes.append(line)
    total_votes=len(votes)

    # count invalid votes
    for vote in votes:
        if vote[-2] != "," or vote[-1] != "1":
            invalid = invalid +1
            votes.remove(vote)
    valid_votes = len(votes)

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
    pap_percent = "{0:0.2f}".format(pap_votes / valid_votes * 100)+"%"
    wp_percent = "{0:0.2f}".format(wp_votes / valid_votes * 100)+"%"
    rp_percent = "{0:0.2f}".format(rp_votes / valid_votes * 100)+"%"
    sda_percent = "{0:0.2f}".format(sda_votes / valid_votes * 100)+"%"

    #make a list of party, votes and percentage
    countedvotes =[["PUNGGOL EAST SMC","PAP",pap_votes,pap_percent],['',"WP",wp_votes,wp_percent],
                   ['',"SDA",sda_votes,sda_percent],['',"RP",rp_votes,rp_percent]]

    #determine winner
    winnerlist =[]
    for counted in countedvotes:    
        winnerlist.append(counted[2])
        if counted[2] == sorted(winnerlist)[-1]:
            winner = counted[1]
    
    #====output to screen====
    
    #write time and date
    print("DATE:"+date + ' '* 20 + "TIME:"+time)

    print("------------------------------------------------")
    print("RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION")
    print("WARD                PARTY     #VOTES    %VOTES")

    for countedvote in countedvotes:
        print(str(countedvote[0]).ljust(20) + countedvote[1].ljust(10) + str(countedvote[2]).ljust(10) + str(countedvote[3]).ljust(5))
    print("------------------------------------------------")

    print("WINNER: "+winner)
    print("TOTAL VOTES: "+str(total_votes))
    print("#SPOILT VOTES: "+ str(invalid))
    print("%SPOILT VOTES: "+ "{0:0.2f}".format(invalid / total_votes * 100)+"%")


    #====output to file====
    outfile.write("DATE:"+date + ' '* 20 + "TIME:"+time+'\n')

    outfile.write("------------------------------------------------"+'\n')
    outfile.write("RESULTS OF THE 2013 PUNGGOL EAST SMC BY ELECTION"+'\n')
    outfile.write("WARD                PARTY     #VOTES    %VOTES"+'\n')

    for countedvote in countedvotes:
        outfile.write(str(countedvote[0]).ljust(20) + countedvote[1].ljust(10) + str(countedvote[2]).ljust(10) + str(countedvote[3]).ljust(5)+'\n')
    outfile.write("------------------------------------------------"+'\n')

    outfile.write("WINNER: "+winner+'\n')
    outfile.write("TOTAL VOTES: "+str(total_votes)+'\n')
    outfile.write("#SPOILT VOTES: "+ str(invalid)+'\n')
    outfile.write("%SPOILT VOTES: "+ "{0:0.2f}".format(invalid / total_votes * 100)+"%")

    infile.close()
    outfile.close()

except IOError:
    print("cannot read from VOTES.DAT or cannot write to RESULTS.DAT")
