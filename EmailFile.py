#
# Read the newly posted questions on the SAP Community Network,
# Show a snap shot of all the Q&A
#
import urllib.request
import re
import os.path
from datetime import datetime
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://answers.sap.com/index.html')

#get the result code and print it, 200 means success
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()

#get current date and time
now = datetime.now()
#format the date and time to suit a file name
dt_string = now.strftime("%B %d, %Y")


#Open the file and pass data to be written.
mailSubject = "SCN: Questions Daily Digest ("+dt_string+")"
email_content="</br>"

#  retrieve all the div tags with a paritcular css element on the page
divs = re.findall(r'<div class="dm-contentListItem__title">(.*?)</div>',str(data))
# loop for retrieving div tags
for eachDiv in divs:
    hrefS = re.findall(r'title=(.*?)>', str(eachDiv))
    for hRef in hrefS: # loop for retrieving only titles in the relevent divs
        email_content = email_content+"<br/>"+hRef
sign_content ="<br/>"+"Thanks,"+"<br/>"+"Jakes"
message = Mail(
    from_email='abcd@gmail.com',
    to_emails='xyz@gmail.com',
    subject=mailSubject,
    html_content=email_content+sign_content)
try:
    sg = SendGridAPIClient(os.environ.get('SG API Key'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)