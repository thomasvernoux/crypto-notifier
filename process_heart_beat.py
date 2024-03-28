


from functions_email import *





def ProcessHeartBeat():
    print("heart beat")
    body = "crypto-notifier heart beat"
    subject = body
    send_email(subject, body)

