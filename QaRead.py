#
# Read the newly posted questions on the SAP Community Network,
# Show a snap shot of all the Q&A
#
import urllib.request
import re
import os.path
from datetime import datetime
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://answers.sap.com/index.html')

#get the result code and print it, 200 means success
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()

#get current date and time
now = datetime.now()
#format the date and time to suit a file name
dt_string = now.strftime("%d %m %Y_%H %M %S")
#create a file with timestamp to avoid overwritting
cust_dir = 'D:/'
file_name = 'SCN_'+"_"+dt_string
completeName = os.path.join(cust_dir, file_name+".txt")

#Open the file and pass data to be written.
file1 = open(completeName, "w")
toFile = "SCN: Questions of the Day!"+\
         "\n"+"**************************""\n"
file1.write(toFile)

#  retrieve all the div tags with a paritcular css element on the page
divs = re.findall(r'<div class="dm-contentListItem__title">(.*?)</div>',str(data))
# loop for retrieving div tags
for eachDiv in divs:
    hrefS = re.findall(r'title=(.*?)>', str(eachDiv))
    for hRef in hrefS: # loop for retrieving only titles in the relevent divs
        print(hRef)
        file1.write(hRef+"\n")

#close file write
file1.close()