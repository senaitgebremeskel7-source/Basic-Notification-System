from factory import NotificationFactory
from email_service import EmailService
from sms_service import SMSService

if __name__ == "__main__":
    factory = NotificationFactory()

    # Register services
    factory.register_service("email", EmailService)
    factory.register_service("sms", SMSService)

    # Use services
    email = factory.create_service("email")
    email.send("user@example.com", "Hello from Email Service!")

    sms = factory.create_service("sms")
    sms.send("+1234567890", "Hello from SMS Service!")

    print(" All notifications sent successfully!")
