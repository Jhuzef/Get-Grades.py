# Get-Grades.py
<h3>Summary</h3>
This script was made to automate the process of checking grades at the end of the semester for NJIT student. It mainly uses the Mechanize and BeautifulSoup libraries to authenticate and parse the NJIT website for grades.
<br>
A notification will be sent to the OS, assuming Mac OS, using a line of AppleScript, and through e-mail using the smtplib library. Gmail requires that you allow 'less-secure apps' to grant this script privilege to send e-mails.
<br>
This script looks for the keyword "Grade posted" on the announcements table to determine when a grade has been posted or not. Using a regular expression, if the keyword is found, then the script notifies the user.
<br>
I recommend running this script as a cronjob in the background to optimize the convenience.
<br><br>
<b>Limitations</b><br>
The script will always notify you that a grade has been posted for as long as that announcement is on the homepage. I highly recommend clearing the announcement to keep yourself from being sent more notification.
<br>
It requires that you hardcode your credentials. From a security point of view, this is very bad practice. It's one of those times where you, the user, must choose either convenience or security.
<br><br>
<b>Quick Tip</b><br>
Don't forget to replace the {{ variables }} with your information.
