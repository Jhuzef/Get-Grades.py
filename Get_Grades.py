#!/usr/bin/env python

import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import re
import smtplib
import os

def notify(title, text):
    #Only works for Mac
     os.system("""
              osascript -e 'display notification "{}" with title "{}"' 
              """.format(text, title))
	# Establish a secure session with gmail's outgoing SMTP server
     server = smtplib.SMTP( "smtp.gmail.com", 587 ) #Assuming gmail
     server.starttls()

     #Input the e-mail sender
     server.login( '{{ SENDER EMAIL }}', '{{ SENDER EMAILS PASSWORD }}' )

     message = 'Subject: {}\n\n{}'.format("Joseph's Notification Bot", "A grade has been posted to the NJIT website.")

   #Input the e-mail to receive the message
     server.sendmail( "Joseph's notification Bot", ' {{ RECIPIENT EMAIL }}', message)
     server.quit()


cj = cookielib.CookieJar()
br = mechanize.Browser()

#input your NJIT credentials
username = "{{ USERNAME }}"
password = "{{ PASSWORD }}"

br.set_cookiejar(cj)

br.open("https://www6.njit.edu/cp/login.php")

br.select_form("cplogin")
br.form['pass'] = password


br.form.new_control('hidden', 'user', {'value': username})
br.form.fixup()

br.submit()

#Redirect to the home page after authentication
br.open("https://cp4.njit.edu/cp/home/next")

#Grab the contents of the webpage and searches for the key word 'Grade posted for'
soup = BeautifulSoup(br.response().read(), "lxml")
for hit in soup.findAll(attrs={'class' : 'uportal-channel-text'}):
	if re.search("Grade posted for", str(hit)):
		notify("Grade Posted", "A grade has been posted to the NJIT website.")
		break
