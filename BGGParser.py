#!/usr/bin/env python
# coding=utf-8-
import csv
import cgi
#Import cgi trackback module for debugging
import cgitb
# Enable debugging
cgitb.enable()

print "Content-Type: text/html; charset=utf-8\n"

print "<html><head><title>WorkPls</title>\n</head><body>\n"

print "<h1>Hello world please hear me. I am still alive</h1>\n"
print "</body></html>"
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



#returns true if overrated, false if equal or underrated when compared to the average bgg rating
def compareRatings(DReader):
    gameDict = dict()
    for row in DReader:
        gameDict[row['objectname']] = float(row['rating'])>float(row['average'])

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
def printRatedLists(gameList):
    stringy = ""
    for game in gameList:
        stringy+= game +"<br> "
    return stringy

### Tiny data analysis functions here ###

#returns a dictionary that only has the object name, rating, and average bgg rating, complexity weight, and BGG Ranking
def getSmallDict(DReader):
    gameDict = dict()
    for game in DReader:
        gameDict[game['objectname']] = dict(rating = game['rating'], average = game['average'],weight = game['avgweight'], rank = game['rank'] )
    return gameDict


#Reads in and returns smaller compressed dictionary for ease of access and manipulation
def readAndCompress(fileName):
    with open(fileName) as csvdata:
        collection = readCollectionCSV(csvdata)
        tinyData = getSmallDict(collection)
        csvdata.close()
        return tinyData


### Down here is the Main execution zone for testing, etc.###

with open('collection.csv') as csvdata:
    collection = readCollectionCSV(csvdata)
    form = cgi.FieldStorage()

    item = form.getvalue('op')
    if item != item:
        print 'Error - You didn\'t select an operation!'
        
    if item == "myAvg":
        print '<h1>This is your Average Rating </h1>'
        print "<p>",myAvgRating(collection),"</p>"
    elif item == "under":
        print '<h1>These are games you like less than the community on average. </h1>'
        print "<p>",printRatedLists(getUnderrated(compareRatings(collection))),"</p>"
    elif item == "over":
        print '<h1>These are games you like more than the community on average.</h1>'
        print "<p>",printRatedLists(getOverrated(compareRatings(collection))),"</p>"
    elif item == "debug":
        print "<p> Oh Hi, you've done at thing on the server!</p>"

    print '<a href="index.html">Return Home</a>'
    print "</body></html>"



