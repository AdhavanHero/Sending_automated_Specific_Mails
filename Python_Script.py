import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

email = os.environ.get('EMAIL')
api_key = os.environ.get('API_KEY')

# Set up the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = 'Superhero8871@gmail.com'
smtp_password = 'rsnsvxmdbioivlqc'

# Create a message object and set the message content

my_array = [
    {"email": "ap4992@srmist.edu.in", "Cont": "Hi dude","mission":"save the world"},
    {"email": "adhavanponram@gmail.com", "Cont": "Hi Adhavan","mission":"Never give up"},
    {"email": "Superhero8871@gmail.com", "Cont": "Hi Hero","mission":"win the war at any cause"}
    ]
# Loop through the array and print the contents of each dictionary
for item in my_array:
        def message(Var1,Var2,Var3):
            message = MIMEMultipart()
            message["From"] = email
            message["To"] = item["email"]
            message["Subject"] = item["mission"]
            message_text = item["Cont"]
            message.attach(MIMEText(message_text))
            smtp_client = smtplib.SMTP(smtp_server, smtp_port)
            smtp_client.ehlo()
            smtp_client.starttls()
            smtp_client.login(smtp_username, smtp_password)
            smtp_client.sendmail(message["From"], message["To"], message.as_string())
            smtp_client.quit() 
        message(item["mission"],item["email"],(item["Cont"]))                                                 
print('Array printed!')



