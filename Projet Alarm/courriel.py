import smtplib
from log import *

class email: 
    #Information du email (Sender)
    SMTP_USER = "202195882@collegeahuntsic.qc.ca" 
    SMTP_PASSWORD = "s891006W" 
    SMTP_SERVER = "smtp-mail.outlook.com" 
    SMTP_PORT = 587 

    emailFrom = str 
    nameFrom = str 
    emailTo = str 
    nameTo = str 

    def __init__(self, emailFrom, nameFrom, emailTo, nameTo):
       
        self.emailFrom = emailFrom 
        self.nameFrom = nameFrom 
        self.emailTo = emailTo 
        self.nameTo = nameTo 
        self.log = logHistory()

    def send(self, objet, msg): 

        entete = ( 
            "From: " + self.nameFrom + " <" + self.emailFrom + ">\n" 
            "To: " + self.nameFrom + " <" + self.emailTo + ">\n" 
            "Subject:" + objet + "\n\n" 
            ) 

        print(entete + msg) 
        try: 
            #Formatage du e-mail
            server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)  
            server.starttls() 
            server.login(self.SMTP_USER, self.SMTP_PASSWORD) 
            server.sendmail(self.emailFrom, self.emailTo, (entete + msg)) 
            server.close() 

        except smtplib.SMTPException: 
            self.log.error("Impossible d'envoyer le mail a " + self.emailTo)
        except (smtplib.socket.error, smtplib.SMTPConnectError): 
            self.log.error("Connexion impossible au serveur SMTP")
