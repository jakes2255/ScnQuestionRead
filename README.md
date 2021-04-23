# SAP Developer Community Daily Digest

![alt text](https://img.shields.io/badge/Python-3-lightgrey "Python 3")
![alt text](https://img.shields.io/badge/SCN-Bot-yellowgreen "SCN Bot")
![alt text](https://img.shields.io/badge/Task-Automate-orange "Automation")
![alt text](https://img.shields.io/badge/Email-Notify-red "e-mail")
![alt text](https://img.shields.io/badge/Style-Content-green "content")

Daily Email Notification from SAP Developer Community!

By Arun Jacob

<!---![Email Notification](https://cdn.pixabay.com/photo/2017/11/17/09/37/businessman-2956974_960_720.jpg)-->
<p align="center">
  <img width="460" height="300" src="https://cdn.pixabay.com/photo/2017/11/17/09/37/businessman-2956974_960_720.jpg"><br>
  Image by <a href="https://pixabay.com/users/geralt-9301/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2956974">Gerd Altmann</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2956974">Pixabay</a>
</p>

## Overview

The goal of this personal project is to set up an Automated Email Notificaion mechanism that reads the latest Questions and Answers published on SAP Developer Community to specified email ids of users. Using data on questions and answeres scrapped from Sap.com, core content of the email is generated.

![SCN Daily Digest](https://github.com/jakes2255/ScnQuestionRead/blob/8c6dbc333df128c0a48340a172b43285aaae8909/img/SCN%20Daily%20Digest%20Desktop%20Version.png)
## Get Data/Questions

Open a connection to the URL, https://answers.sap.com/index.html using urllibData.

Once the connection is established, Http Status code: 200 is returned and we proceed to filter the HTML Data. The questions and answers follows a specific pattern in the DOM and after carefully examinining the same, we derive the pattern used here. Another Python library for Regular Expressions is used to get all the spcific items in an Array/List.

By looping over the above created Array, we generate the content with Title, link, description etc. For getting richer content we have utilized BeautifulSoup library for scrapping the data and form the email content.

Read Sap Community Network(SCN) Questions by using Python3 Libaries in less than 10 lines of code.

Would it be interesting if we could automate the task of monitoring a website of interest to check for possible updates?
This partcular application written in Python3 achieves the task of reading the SCN community for latest questins being asked.

Can be tailored for further useful HTML tags.:relaxed:

## SCN Blogs

[Simple SCN Bot in 10 lines using Python](https://blogs.sap.com/2019/08/25/simple-scn-bot-in-10-lines-using-python/)

[Automating SCN Question Read](https://blogs.sap.com/2019/08/29/automating-scn-question-read/)

[Emal Notification](https://blogs.sap.com/2019/08/30/scn-automated-email-notification/)

[Email Content](https://blogs.sap.com/2019/09/05/web-scraping-with-python-to-beautify-email/)

## Epilogue
    The below summarizes why we need a daily digest!!!
![Email Notification](https://github.com/jakes2255/ScnQuestionRead/blob/master/img/dailyMotivation.jpg)

Thanks,</br>
Arun
