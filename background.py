#! /usr/bin/python
import json, urllib2, urllib
import os
import datetime
import io
 
dt = datetime.datetime.now()
cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)
api="http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-IN"
response=urllib2.urlopen(api)
jsn=json.load(response)
imgUrl=jsn['images'][0]['url']
url="http://www.bing.com"+imgUrl
name="desk"+cd+".jpg"
if not os.path.exists("Bing"):
    os.makedirs("Bing")
urllib.urlretrieve(url,"Bing/"+name)
os.system('gsettings set org.gnome.desktop.background picture-uri file:////home/hari/Programs/Bing/'+name)
