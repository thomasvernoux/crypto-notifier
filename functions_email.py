"""
functions : 
send_email(subject, body)

"""
import smtplib
from email.mime.text import MIMEText
from global_variables import *


recipients = ["thomas@vernoux.be"]
sender = "thomasvernouxsmtp@gmail.com"
password = "jych cyvw ncyy fmmt"



def send_email(subject, body):
   """
   Sent an email to thomas@vernoux.be
   """

   msg = MIMEText(body)
   msg['Subject'] = subject
   msg['From'] = sender
   msg['To'] = ', '.join(recipients)
   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
      smtp_server.login(sender, password)
      smtp_server.sendmail(sender, recipients, msg.as_string())
      
   print("Message sent!")  

   
            
   
      



    


