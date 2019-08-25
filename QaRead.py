#
# Read the newly posted questions on the SAP Community Network,
# Show a snap shot of all the Q&A
#
import urllib.request
import re
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://answers.sap.com/index.html')

#get the result code and print it, 200 means success
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()

#  retrieve all the div tags with a paritcular css element on the page
divs = re.findall(r'<div class="dm-contentListItem__title">(.*?)</div>',str(data))
# loop for retrieving div tags
for eachDiv in divs:
    hrefS = re.findall(r'title=(.*?)>', str(eachDiv))
    for hRef in hrefS: # loop for retrieving only titles in the relevent divs
        print(hRef)