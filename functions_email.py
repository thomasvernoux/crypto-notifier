"""
functions : 
send_email(subject, body)
Author : Thomas Vernoux
Date : March 3, 2024
"""
import smtplib
from email.mime.text import MIMEText
from global_variables import *
from functions_log import *
import inspect

recipients = ["thomas@vernoux.be"]
sender = "thomasvernouxsmtp@gmail.com"
password = "jych cyvw ncyy fmmt"



def send_email(subject, body):
   """
   Sent an email to thomas@vernoux.be
   """

   log_trace(str(inspect.currentframe().f_back.f_code.co_name))
   msg = MIMEText(body)
   msg['Subject'] = subject
   msg['From'] = sender
   msg['To'] = ', '.join(recipients)
   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
      smtp_server.login(sender, password)
      smtp_server.sendmail(sender, recipients, msg.as_string())
      
   print("Message sent!")  

   
            
   
      



    


