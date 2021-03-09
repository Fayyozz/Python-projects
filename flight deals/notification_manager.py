from twilio.rest import Client
import smtplib
TWILIO_SID = 'ACfc5672db37b86b7101318c7e6c69faff'
TWILIO_AUTH_TOKEN = '4b49dbf9c08d7c6d28c5b3b641752b79'
TWILIO_VIRTUAL_NUMBER = '+19284474635'
TWILIO_VERIFIED_NUMBER = '+998915228512'
sender_email = "00010847f@gmail.com"
password = input("Enter your password and press enter: ")
smtp_server = "smtp.gmail.com"
port = 587


class NotificationManager:

    def __init__(self, ):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, receiver, message):
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(user=sender_email, password=password)
            server.sendmail(from_addr=sender_email, to_addrs=receiver, msg=message)

