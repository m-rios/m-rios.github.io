from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import simplejson

import smtplib
from email.mime.text import MIMEText


PORT = 8000

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


class MyHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.send_response(200)
        self.end_headers()

        data = simplejson.loads(self.data_string)
        send_email(data["email"], data["name"], data["msg"])
        return

    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type',    'text/html')
        self.end_headers()
        self.wfile.write("<html><body>Hello world!</body></html>")
        self.connection.shutdown(1)

Handler = MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
