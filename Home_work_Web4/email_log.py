import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_to_email():
    fromaddr = "pepe1@mail.ru"
    toaddr = "pepe1@mail.ru"   #testgb112@mail.ru
    mypass = "u3buCfLD9RBpfBkyiG8P"  #uagNc1x9bkdASwHyDr1D
    reportname = "report.html"
    msg = MIMEMultipart('alternative')
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Привет это питон"
    body = "Это пробное сообщение"

    # with open(reportname, "rb", encoding='utf-8') as f:
    #     part = MIMEApplication(f.read(), Name=basename(reportname))
    #     part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)
    #     msg.attach(part)
    with open(reportname, "r", encoding='utf-8') as f:
        report_text = f.read()

    body += report_text

    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()