from urllib import request
from bs4 import BeautifulSoup

url = "http://builds.be.softathome.com/releases/REL/"
html = request.urlopen(url).read()


html_parsed = BeautifulSoup(html, features="html.parser")

projectList = []
for link in html_parsed.find_all('a'):
    projectList.append(link.get_text())
projectList.remove('Name') 
projectList.remove('Last modified')
projectList.remove('Size')
projectList.remove('Description')
projectList.remove('Parent Directory')
for elt in projectList:
    print(elt)

# import os

# print(os.getcwd())

# print(os.path.normpath(os.getcwd() + os.sep + os.pardir+ os.sep + os.pardir))