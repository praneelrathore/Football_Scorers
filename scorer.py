import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep
def sendMessage(title,message):
	pynotify.init("Test")
	notice = pynotify.Notification(title,message)
	notice.show()
	return

url = "http://www.scorespro.com/rss2/live-soccer.xml"

while True:
	r=requests.get(url)
	while r.status_code is not 200:
		r=requests.get(url)
	s=BeautifulSoup(r.text)
	data=s.find_all("description")
	score=data[1].text
	sendMessage("Score",score)
	sleep(60)
