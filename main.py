from WebsiteClass import Website

initialAction = int(input("What do you wish to do: 1. Make a new webSite. 2. Edit an old save"))


if initialAction == 1:
    newWebsite = Website()
    newWebsite.create()
