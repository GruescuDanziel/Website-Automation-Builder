from WebsiteClass import Website
from questions import questions

import PyInquirer as pi

initialAction = int(input("What do you wish to do: 1. Make a new webSite. 2. Edit an old save"))


if initialAction == 1:
    newWebsite = Website()
    newWebsite.create()
    while(newWebsite.editing):
        userChoice = pi.prompt(questions[0])['choice']
        getattr(newWebsite, userChoice)()
