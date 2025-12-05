class Notification:
    def send(self,message):
        print("Sending notiication : ",message)

class EmailNotification(Notification):
    def send(self,message):
        print("Sending email to user: ",message)

class SMSNotification(Notification):
    def send(self,message):
        print("Sending SMS to user: ",message)

class PushNotification(Notification):
    def send(self,message):
        print("Sending push notification to user: ",message)


#usage
n1=EmailNotification()
n1.send("Mail Sent")

n2=SMSNotification()
n2.send("OTP is 4837")

n3=PushNotification()
n3.send("You have a message")