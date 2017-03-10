#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      OluwakemiOmotunde
#
# Created:     06/03/2017
# Copyright:   (c) OluwakemiOmotunde 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#load our modules
import sys
import urllib2 # used to load url

#obtain an article from the web. I chose something I was interested in, housing in NYC
url = "http://www.myrecipes.com/recipe/jambalaya"
url_open = urllib2.urlopen(url)
text = url_open.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(text)

webtext = ""
def getText(soup):
    return webtext.join(soup.findAll(text = True)).encode('ascii', 'ignore')

myText = [getText(n) for n in soup.findAll(["p"])] #this works

#Create on long string from myText

myText_str = "".join(myText) #this works

#This part took me four days to complete. I finally realized why my import was not working.
#I had to pip install and change the destination.


from watson_developer_cloud import AlchemyLanguageV1
AL = AlchemyLanguageV1(api_key='51ce17b02658f61d14925ee20733c1bf6979a10d')
result = AL.keywords("text", myText_str)

print('') #space

print("Top 10 Key Words")

#now to get top 10

index = 1;
for keyword in result['keywords']:
    print(index) #what rank  it is
    print('Word: ', keyword['text'].encode('utf-8'))
    print('Relevance: ', keyword['relevance'].encode('ascii', 'ignore'))
    print('')
    index = index + 1

#I did not get the correct result and would appreciate if you could point out where I went wrong.