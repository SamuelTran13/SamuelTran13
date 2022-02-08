# Tran Program 1 baseball stuff

name = input('Enter player name: ')
atBats = int(input('Enter the number of at bats: '))
hits = int(input('Enter the number of hits: '))

# See wikipedia for details on computing batting averages
# BA is the batting average

BA = hits/atBats

print('Batting average for ', name, 'is: ', format(BA, '.3f'))
