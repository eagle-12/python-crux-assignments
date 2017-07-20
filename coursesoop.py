import requests
import getpass
from bs4 import BeautifulSoup

class Scraper:
	"""a class to access the cms"""
	def __init__(self,url,username,password):
	        """to convert username and password to usable form"""
		self.url = url
		self.username = username
		self.password = password
		self.values = {'username':username,'password':password}
	
	def formsubmit(self,url1=""):
	        """to create a session and get the contents of the webpage"""
		if url1:
			url1 = url1
		else:
			url1 = self.url	
		self.s = requests.Session()
		self.s.post(self.url,self.values)
		self.r = self.s.get(url1)
	
	def get_courses(self):
	        """to scrape the web page and to print all the courses"""
		self.soup = BeautifulSoup(self.r.content,'html.parser')
		for course in self.soup.select('h2.title > a'):
			print(course.get_text())	
			

print "enter username",
username = raw_input()
password = getpass.getpass("enter password ")
scrape = Scraper('http://id.bits-hyderabad.ac.in/moodle/login/index.php',username,password)
scrape.formsubmit("http://id.bits-hyderabad.ac.in/moodle/my/index.php?mynumber=-2")
scrape.get_courses()			
