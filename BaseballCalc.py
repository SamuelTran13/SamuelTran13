#Samuel Tran
#December 8, 2021
#COSC 1336 - Hooper
#Project 10 - Baseball Stats
#This module contains all the calculations needed for Project 10. Each stat
#is explained below.

def BA(stats, results):
    #Batting Average (BA) is equal to the quotient between hits divided by at bats
    i = 0
    while i< len(stats):
        batAve = format(int(stats[i][7])/int(stats[i][5]), ',.3f')
        results[i].append(batAve)
        i+=1

def slugPercent(stats, results):
    #Slugging Percentage (SP) takes into account the value of hits and is the sum
    #of the values of hits divided by the number of times at bat
    i = 0
    doubles = int(stats[i][8])
    triples = int(stats[i][9])
    homers = int(stats[i][10])
    while i < len(stats):
        #Singles is equal to the difference between hits and doubles + triples +
        #home runs 
        singles = int(stats[i][7]) - (doubles + triples + homers)
        
        SP = (singles + 2*doubles + 3*triples + 4*homers)/int(stats[i][5])
        results[i].append(format(SP, ',.3f'))
        i += 1

    return
    
def OBP(stats, results):
    #On base Percentage(OBP) is equal to the sum of hits, bases on balls/walks(BB),
    #and hit by pitches (HBP) divided by the number of plate appearances which
    #is equal to the sum of at bats, BB, HBP, and sacrific flys
    i = 0
    hits = int(stats[i][7])
    BB = int(stats[i][12])
    HBP = int(stats[i][16])
    while i < len(stats):
        OBP = (hits + BB + HBP)/ (int(stats[i][5])+ BB + HBP + int(stats[i][17]))
        results[i].append(format(OBP, ',.3f'))
        i +=1
        
    return

def OPS(stats,results):
    #OPS stands for on base percentage (OBP) plus slugging percentage (SP)
    i = 0
    while i < len(stats):

        #Calculate Slugging percentage (SP)
        doubles = int(stats[i][8])
        triples = int(stats[i][9])
        homers = int(stats[i][10])
        singles = int(stats[i][7]) - (doubles + triples + homers)
        SP = (singles + 2*doubles + 3*triples + 4*homers)/int(stats[i][5])

        #Calculate On base percentage (OBP)
        hits = int(stats[i][7])
        BB = int(stats[i][12])
        HBP = int(stats[i][16])
        OBP = (hits + BB + HBP)/ (int(stats[i][5])+ BB + HBP + int(stats[i][17]))
        
        OPS = SP + OBP
        results[i].append(format(OPS, ',.3f'))
        i += 1
    
    return

def RP(stats, results):
    #Runs produced(RP) is calculated by getting sum of runs and runs batted in
    #and subtracting home runs
    i = 0
    while i < len(stats):
        RP = int(stats[i][6]) + int(stats[i][11]) - int(stats[i][10])
        results[i].append(RP)
        i += 1

    return

def RPAtBat(stats, results):
    #Runs produced for at bats(RPAtBat) is equal to runs produced (RP) divided
    #by at bats
    i = 0
    while i < len(stats):
        #Calculate Runs produced (RP)
        RP = int(stats[i][6]) + int(stats[i][11]) - int(stats[i][10])
        
        RPAtBats = RP/int(stats[i][5])
        results[i].append(format(RPAtBats, ',.3f'))
        i += 1

    return







