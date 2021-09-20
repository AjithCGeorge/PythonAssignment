import smtplib, ssl


# sender_email = ajithpythonassignmet@gmail.com
# password = pythonassignment


def sendMail(sender_email,receiver_email,password,message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


sender_email=input("Enter the senders's mail id : ")
password=input('enter the password to the senders mail id : ')
receiver_email=input('Enter the recivers mail id : ')
sub=input('Enter the subject of the email : ')
content=input('Enter the content of the email : ')

message = """\
    Subject: {}

    {}.""".format(sub,content)
sendMail(sender_email,receiver_email,password,message)