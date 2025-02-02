# import pandas lib as pd
import pandas as pd

# import smtp lib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email SMTP Credentials
senderEmail = 'user@gmail.com'
senderPassword = 'ijft khgm lwur ncga'

# Email Subject
emailSubject = 'Subject line here.'


def getEmailTemplate():
  # Read email body from text file
  file = open('emailTemplate.txt', 'r')
  return file.read()

def getEmailContent(template, name):
  # Replace receiver name with placeholder
  return template.replace('----- ', name)

def sendEmail(toEmail, template):
  message = MIMEMultipart()
  message["To"] = toEmail
  message["From"] = senderEmail
  message["Subject"] = emailSubject

  title = '<b> Title line here. </b>'
  # messageText = MIMEText('''Message body goes here.''','html')
  # messageText = MIMEText(template, 'html')
  messageText = MIMEText(template, 'plain')
  message.attach(messageText)

  # email = senderEmail
  # password = senderPassword

  server = smtplib.SMTP('smtp.gmail.com:587')
  server.ehlo('Gmail')
  server.starttls()
  server.login(senderEmail, senderPassword)
  fromaddr = senderEmail
  toaddrs  = toEmail
  server.sendmail(fromaddr, toaddrs, message.as_string())

  server.quit()


# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('emails.xlsx')

template = getEmailTemplate()

for index, row in dataframe1.iterrows():
  print('Name: ' + row['Name'] + '\nEmail: ' + row['Email'])
  emailContent = getEmailContent(template, row['Name'])
  # print(emailContent)
  sendEmail(row['Email'], emailContent)

