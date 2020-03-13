#Send emails through SMTP>-------------------------------
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'bob-roswell-1947@gmail.com'
msg['To'] = 'zultron@thebigeye.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('127.0.0.1',1025)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('me@gmail.com', 'mypassword')

mailserver.sendmail('me@gmail.com','you@gmail.com',msg.as_string())

mailserver.quit()

