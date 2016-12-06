import smtplib
from email.mime.text import MIMEText

def send_email(address, name, in_msg):
    msg = MIMEText(in_msg)
    msg['Subject'] = 'Contact form from %s address: %s' % (name, address)
    msg['From'] = "utopianrobotics@gmail.com"
    msg['To'] = "utopianrobotics@gmail.com"

    gmail_user = "utopianrobotics@gmail.com"
    gmail_pwd = "YoQueSe2016:)"
    FROM = "utopianrobotics@gmail.com"
    TO = "utopianrobotics@gmail.com"

    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"


send_email("mrm994@gmail.com", "Mario", "Mensaje mazo secreto")
