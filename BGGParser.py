import csv



#reads in a CSV file as a dictionary using the csv module's DictReader
def readCollectionCSV(fileName):
    bggCSV = csv.DictReader(fileName)
    return bggCSV


#below here are various methods that perform calculations on game ratings.
#Most of these can be used on their own

#returns the average of user ratings. Takes a DictReader as input
def myAvgRating(DReader):
    entries = 0
    total = 0

    for row in DReader:
        total += float(row['rating'])
        entries +=1
    return total/entries


def getDictColumnValues(columnName):
    print("columnName TODO")

#returns true if overrated, false if equal or underrated when compared to the average bgg rating
def compareRatings(DReader):
    gameDict = dict()
    for row in DReader:
        gameDict[row['objectname']] = float(row['rating'])>float(row['average'])

    return gameDict

#returns a dictionary that only has the object name, rating, and average bgg rating
def getSmallDict(DReader):
    gameDict = dict()
    for game in DReader:
        gameDict[game['objectname']] = dict(rating = game['rating'], average = game['average'],weight = game['avgweight'], rank = game['rank'] )
    return gameDict
def getOverrated(gameDict):
    overList = []
    for game in gameDict:
        if gameDict[game]:
            overList.append(game)
    return overList

def getUnderrated(gameDict):
    underList = []
    for game in gameDict:
        if not gameDict[game]:
            underList.append(game)
    return underList

#Reads in and returns smaller compressed dictionary for ease of access and manipulation
def readAndCompress(fileName):
    with open(fileName) as csvdata:
        collection = readCollectionCSV(csvdata)
        tinyData = getSmallDict(collection)
        csvdata.close()
        return tinyData


### Down here is the Main execution zone for testing, etc.###
def main():
    tinyData = readAndCompress('collection.csv')

        
    print tinyData


main()
    


