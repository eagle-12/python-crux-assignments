import requests
url = 'http://id.bits-hyderabad.ac.in/moodle/login/index.php'
import getpass
print "enter username",
username = raw_input()
password = getpass.getpass("enter password ")
values = {'username':username,'password':password}
s = requests.Session()
s.post(url,values)
r = s.get("http://id.bits-hyderabad.ac.in/moodle/my/index.php?mynumber=-2")
#r = requests.post(url, data=values)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content,'html.parser')
for course in soup.select('h2.title > a'):
	print(course.get_text())
