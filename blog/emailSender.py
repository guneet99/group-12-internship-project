import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 
def emailSender(add,message,subject):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('fitzone.transformation@gmail.com','jkbkienvdvxqbpzw')
    msg = MIMEMultipart()
    msg['From'] = 'fitzone.transformation@gmail.com'
    msg['To'] = add
    msg['Subject'] = subject 
    msg.attach(MIMEText(message))
    server.send_message(msg)
    server.quit()

def emailSenderWithAttach(add,message,subject,ref):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('fitzone.transformation@gmail.com','jkbkienvdvxqbpzw')
    msg = MIMEMultipart()
    msg['From'] = 'fitzone.transformation@gmail.com'
    msg['To'] = add
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    filename = "GFG.pdf"
    attachment = open("C:/Users/home/Desktop/django_web_app/"+ref, "rb")
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    server.send_message(msg)
    print("email sent")
    server.quit() 

def emailSenderWithAttachDiet(add,message,subject):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('fitzone.transformation@gmail.com','jkbkienvdvxqbpzw')
    msg = MIMEMultipart()
    msg['From'] = 'fitzone.transformation@gmail.com'
    msg['To'] = add
    msg['Subject'] = subject
    msg.attach(MIMEText(message))
    filename = "Diet Plan.doc"
    attachment = open("C:/Users/home/Desktop/django_web_app/Diet Plan.doc", "rb")
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    server.send_message(msg)
    print("email sent")
    server.quit() 