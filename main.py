from factory import NotificationFactory        # Import NotificationFactory class
from email_service import EmailService         # Import EmailService class
from sms_service import SMSService             # Import SMSService class

if __name__ == "__main__":                     # Run this part only if file is executed directly
    factory = NotificationFactory()            # Create factory object

    # Register services
    factory.register_service("email", EmailService)  # Register Email service in factory
    factory.register_service("sms", SMSService)      # Register SMS service in factory

    # Use services
    email = factory.create_service("email")          # Create email service instance
    email.send("senaitgebremeskel7@gmail.com", "Hello from Email Service!")  # Send email

    sms = factory.create_service("sms")              # Create SMS service instance
    sms.send("+251914823112", "Hello from SMS Service!")  # Send SMS

    print(" All notifications sent successfully!")    # Print success message
