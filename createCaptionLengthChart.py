import csv
import matplotlib.pyplot as plt
import re

#Return the number of words in a caption
def wordCount(caption):
    return len(caption.split(" "))

#return a list of all words in a caption
#def wordList(caption):
#    return [word.strip("") for word in caption.split(" ")]

musicFile = open("musiccaps-filtered.csv","r")
musicFile.readline() #Empty out first line
captionRead = csv.reader(musicFile,delimiter=",",quotechar="\"")


x = []
y = []

totals = {}

for row in captionRead:
    aspectList = [word.strip("[], .\":;!?'") for word in row[4].split(",")]
    captionList = row[5].split(" ")

    try:
        totals[len(captionList)]+=1
    except:
        totals[len(captionList)]=1
        
musicFile.close()

x = totals.keys()
for key in x:
    y.append(totals[key])

plt.bar(x,y,width=5,color="#002845")
plt.xlabel("Number of words in caption")
plt.ylabel("Occurences")
plt.title("Occurences of each caption length")

#plt.xlim([0,max(x)])

plt.show()