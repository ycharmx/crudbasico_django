import smtplib

class EmailConnection:
    
    def start_smtp(self, email_username, email_password):
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.ehlo()
        self.server.starttls()
        try:
            self.server.login(email_username, email_password)
            print ('LOGIN IS DONE YEYYY, YOU CAN NOW SEND SHIT EMAILS. xD')
            return True
        except smtplib.SMTPHeloError:
            print ('The server responded weird stuff to my login request, please try again')
            return False
        except smtplib.SMTPAuthenticationError:
            print ('Your account name or password is incorrect, please try again using the correct stuff')
            return False
        except smtplib.SMTPException:
            print ('SHIT IS ALL FUCKED THERES NO HOPE THE WORLD IS GOING TO END, HIDEE ')
            return False

    def send_email_new_item(self, FROM, TO, TEXT, item_name):
        SUBJECT = 'New potencial item: %s' % item_name
        try:
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
            self.server.sendmail(FROM, TO, message)
            self.email_number += 1
            print ('Email number '+ str(self.email_number) + ' was sent for the item ' + item_name)

        except smtplib.SMTPRecipientsRefused:
            print ('The email was not sent, the target refused')
            return False
        except smtplib.SMTPServerDisconnected:
            print ('The server is disconnected.')
            return False
        except:
            print ('SHIT HAPPENED DEAL WITH IT')
            return False