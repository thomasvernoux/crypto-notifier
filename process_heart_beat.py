


from functions_email import *





def ProcessHeartBeat():
    print("heart beat")
    subject = "crypto-notifier heart beat"

    body = Variable("heartbeat_message").get()
    send_email(subject, body)

