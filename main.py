import os
import urllib
import re

def downloadFile(url, name):
	#print url
	image = urllib.URLopener()
	image.retrieve(url, name)

def run():
	page = 1
	for page in range (1,102):
		response  = urllib.urlopen('http://calvinhobbesdaily.tumblr.com/page/' + str(page))
		html = response.read()
		postids = re.findall('.*?\id="post-(.*?)\">.*?', html)
		for id in postids:	
			comicurl = re.findall('.*?\"http://calvinhobbesdaily.tumblr.com/image/' + str(id) + '"><img(.*?)\" alt.*?',html)
			name = re.findall('.*?\<time datetime="(.*?)\" pubdate><a rel="bookmark" href="http://calvinhobbesdaily.tumblr.com/post/' + str(id) + '.*?',html)
			comicurl[0] = comicurl[0].replace(' src="','')
			downloadFile(comicurl[0], name[0] + '.gif')

run()
