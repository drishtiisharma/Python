# Create Email, and SMS notification classes with a common method and process all of them using the same piece of code.

class Notif:
    def push(self):
        pass

class Email(Notif):
    def push(self):
        print("Email SENT!")

class SMS(Notif):
    def push(self):
        print("SMS SENT!")

e = Email()
s = SMS()

for x in (e,s):
    x.push()