#
# Read the newly posted questions on the SAP Community Network,
# Show a snap shot(preview) of all the Q&A
# Clip the number of questions to max four items
# Enhance the look and feel of the page
import requests
from bs4 import BeautifulSoup
import re
import urllib.request
from datetime import datetime
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import random
#Retrieve the contents of SCN Q&A page
page = requests.get('https://answers.sap.com/index.html')
#parse the contents using BeautifulSoup
soup=BeautifulSoup(page.text,'html.parser')
#list of questions uses the css class below
hRefs = soup.find(class_='dm-contentList')
#Links with questions
hRef = hRefs.find_all('a')
#print(hRef)
#final item details and counter
itemDetails=''
itemNumber =0

#get current date and time
now = datetime.now()
#format the date and time to suit a file name
dt_string = now.strftime("%B %d, %Y")


#Open the file and pass data to be written.
mailSubject = "SCN Daily Digest ("+dt_string+")"
header_content = '<header><span style="color:lightBlue;font-weight:bold;font-size: 30px">SCN&nbsp;&nbsp;</span>' \
                 '<span style="color:#D0D3D4;font-weight:bold;">DAILY DIGEST</span></header><hr>' \
                 '<p style="color:#AEB6BF;">SAP Questions for You<p>'
email_content=""
image_num = 100
for item in hRef:
    #get title,link of the questions
    title = re.findall(r'title="(.*?)</a>', str(item))
    #print(title)
    if(len(title)>0):
        topic =title[0]
        question = topic.split('">')
        #print(title[0])
        #itemDetails = title[0]
        itemDetails = question[0]
    link = re.findall(r'<a href="/questions/(.*?).html"', str(item))
    if (len(link) > 0 and itemNumber<4): # clip the contents to four items in the email
        #print(link[0])
        #mail subject as the first question
        if(itemNumber == 0):
            mailSubject = itemDetails
        itemNumber = itemNumber+1
        #Open question to get a preview
        url = 'https://answers.sap.com/questions/'+str(link[0])+'.html'
        qnUrl = urllib.request.urlopen(url)
        # read the data from the URL and print it
        data = qnUrl.read()
        #  retrieve the div tags with question body
        divs = re.findall(r'<div class="dm-section-hero--question__body">(.*?)</div>', str(data))
        qnPreviewContent = divs[0]
        #beautify the preview content
        snapShot = qnPreviewContent.replace("\\n"," ")
        #clipping the preview content to shorten email content, 500 characters
        mailPreview = (snapShot[:500] + '.....') if len(snapShot) > 500 else snapShot
        itemDetails ="<h1>"+itemDetails+"</h1>"
        print("Item "+str(itemNumber)+" :"+itemDetails+"\n"+snapShot)
        str_image_num = str(image_num)
        image_content = "https://picsum.photos/id/" + str_image_num + "/100/100"
        readMore = '<p><a href='+url+' target="_blank" style="background-color: orange;color: white;">' \
                                     '<i>Read More</i></a></p>'
        #altring layout for image and content,row alternate
        if(itemNumber % 2) == 0:
            email_content = email_content + "<section style='display: flex;background-color: lightBlue;'>" \
                                            "<article style='flex: auto;padding: 10px;'>" \
                            + '<img src=' + image_content + ' alt="SCN"></article><article style="flex: auto;padding: 10px;">' \
                            + itemDetails + mailPreview + readMore + "</article></section>"
        else:
            email_content = email_content + "<section style='display: flex;'>" \
                                            "<article style='flex: auto;padding: 10px;'>" \
                            + itemDetails + mailPreview + readMore  \
                            + '</article><article style="flex: auto;padding: 10px;"><img src=' + image_content + ' alt="SCN">' \
                            + "</article></section>"

        image_num = random.randint(0, 1000)
sign_content = "<footer style='text-align: left;'><hr><p>Thank You,<br>Jakes</p></footer></body>"
message = Mail(
    from_email='abc@gmail.com',
    to_emails='xyz@gmail.com',
    subject=mailSubject,
    html_content=header_content+email_content + sign_content)
try:
    sg = SendGridAPIClient(os.environ.get('SG Key'))
    response = sg.send(message)
    print(response.status_code)
except Exception as e:
    print(e.message)