from datetime import datetime
from datetime import date 

#Outputs from YOLO will be in a file called BoundingBoxes.txt
#Each line of the file contains the coordinates of a bounding box: 
# ClassID, x_center, y_center, x_width, y_height 

#Define the "line" for checkout of the dining location:
#x_center, y_center, x_width, y_height
#All dummy values for testing purposes as of now
x_center = 1.5      
y_center = 1.5         
x_width = 1         
y_height = 1         

x_upper = x_center - x_width / 2
x_lower = x_center + x_width / 2
y_upper = y_center - y_height / 2
y_lower = y_center + y_height / 2 

def PeopleCounter(fileName):
    numPeople = 0

    readData = open("BoundingBoxes.txt", "r")
    BBoxesList = readData.readlines("\n")
    for eachLine in BBoxesList:
        boundingBox = eachLine.split("\t")
        x_center_b = boundingBox[1]
        y_center_b = boundingBox[2]
        x_width_b = boundingBox[3]
        y_height_b = boundingBox[4]
        #Determine whether the person is in line
        if (x_upper <= x_center_b and x_center_b <= x_lower) \
            and (y_upper <= y_center_b and y_center_b <= y_lower):
            numPeople += 1
    return numPeople 

#Write the result to a text file along with the indication of time 
peopleCount = PeopleCounter("BoundingBoxes.txt")
today_date = (date.today()).strftime("%Y/%m/%d")
time_now = (datetime.now()).strftime("%H:%M:%S")

print("Today date is ", today_date)
print("Current time is ", time_now)

writeOutput = open("PeopleCounter.txt", "w")
writeOutput.write(today_date + "\t" + time_now + "\t" + str(peopleCount))
writeOutput.close()

