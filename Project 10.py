#Samuel Tran
#December 8, 2021
#COSC 1336 - Hooper
#Project 10 - Baseball Stats
#This program takes a file of baseball stats and performs calculations to find
#batting average,slugging percentage, Onbase percentage, On base plus slugging
#percentage, runs produced and runs produced for at bats. A report is generated
#at the end. 
import BaseballCalc 

def main():
    infile = open('BaseballStats.txt', 'r')
    #Creating empty lists
    stats = []
    results = []
    i = 0
    header = infile.readline() #header line from infile is held here
    temp = infile.readline()
    while temp != "":
        stats.append(temp.split())
        
        #Only append the first 4 elements from stats to results, it does not
        #include any stats 
        results.append(stats[i][0:4]) 
        temp = infile.readline()
        i += 1
    infile.close()

    #Calling for the calculations
    BaseballCalc.BA(stats, results)
    BaseballCalc.slugPercent(stats, results)
    BaseballCalc.OBP(stats, results)
    BaseballCalc.OPS(stats, results)
    BaseballCalc.RP(stats, results)
    BaseballCalc.RPAtBat(stats, results)

    #Sorts the list by  OPS from high to low 
    results.sort(key=lambda x:x[7], reverse = True)

    outfile = open('report.txt', 'w')

    count = 0
    outfile.write('In 2018, a study was done amongst baseball players. The ' +
                  'highest valued statistic was concluded to be On base ' +
                  'percentage plus slugging or OPS. These are the top 3 most ' +
                  'highly valued players based on OPS:' + '\n')
                
    while count < 3:
        outfile.write(results[count][1] + '\t' + str(results[count][7]) + '\n')
        count += 1
        
    #Sorts the list by  RP from high to low
    results.sort(key=lambda x:x[8], reverse = True)
    outfile.write('\n')
    outfile.write('While OPS was the most valued individual statistic, ' +
                  'the most valued team statistic amongst players who voted ' +
                  'was the Runs Produced or RP stat. These are the top 5 most ' +
                  'highly valued team players based on RP: ' + '\n')

    count = 0
    
    while count < 5:
        outfile.write(results[count][1] + '\t' + str(results[count][8]) + '\n')
        count += 1
    
    outfile.close()
    
    print('Report generated in file Report.txt')
main()
