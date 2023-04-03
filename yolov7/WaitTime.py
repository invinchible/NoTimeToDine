from datetime import datetime
from datetime import date 

#Outputs from YOLO will be in a file called BoundingBoxes.txt
#Each line of the file contains the coordinates of a bounding box: 
# ClassID, x_top, y_top, x_bottom, y_bottom 
# These are the coordinates of the top left corner and bottom right corner 
#of the bounding box

#Define the "line" for checkout of the dining location:
#x_top, y_top, x_bottom, y_bottom
#All dummy values for testing purposes as of now
x_top = 0
y_top = 0
x_bottom = 640
y_bottom = 640


def isInLine(x1, y1, x2, y2):
    if (x2 <= x_top) \
    or (x_bottom <= x1) \
    or (y2 <= y_top) \
    or (y_bottom <= y2):
        return True
    return False 

def PeopleCounter(fileName):
    numPeople = 0

    readData = open("BoundingBoxes.txt", "r")
    BBoxesList = readData.readlines()
    for eachLine in BBoxesList:
        boundingBox = eachLine.split("\t")
        x1_b = int(boundingBox[1])
        y1_b = int(boundingBox[2])
        x2_b = int(boundingBox[3])
        y2_b = int(boundingBox[4])
        #Determine whether the person is in line
        if  isInLine(x1_b, y1_b, x2_b, y2_b):
            numPeople += 1
    return numPeople 

#Write the result to a text file along with the indication of time 
peopleCount = PeopleCounter("BoundingBoxes.txt")
today_date = (date.today()).strftime("%Y/%m/%d")
time_now = (datetime.now()).strftime("%H:%M:%S")

#print("Today date is ", today_date)
#print("Current time is ", time_now)

writeOutput = open("PeopleCounter.txt", "w")
writeOutput.write(today_date + "\t" + time_now + "\t" + str(peopleCount))
writeOutput.close()

