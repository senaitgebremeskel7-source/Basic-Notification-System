from email_service import EmailService            # Import EmailService class
from sms_service import SMSService                # Import SMSService class
from factory import NotificationFactory           # Import NotificationFactory class

def test_email_service():                         # Function to test EmailService
    service = EmailService()                      # Create EmailService object
    result = service.send("senaitgebremeskel7@gmail.com", "Test Email")  # Simulate sending email
    assert result is True                         # Check if send() returned True
    assert service.service_type == "EMAIL"         # Verify service type is EMAIL

def test_sms_service():                           # Function to test SMSService
    service = SMSService()                        # Create SMSService object
    result = service.send("+1234567890", "Test SMS")  # Simulate sending SMS
    assert result is True                         # Check if send() returned True
    assert service.service_type == "SMS"           # Verify service type is SMS

def test_factory():                               # Function to test NotificationFactory
    factory = NotificationFactory()                # Create factory object
    factory.register_service("email", EmailService)  # Register EmailService
    factory.register_service("sms", SMSService)      # Register SMSService

    email = factory.create_service("email")          # Create email service instance
    sms = factory.create_service("sms")              # Create sms service instance

    assert isinstance(email, EmailService)           # Check email is correct type
    assert isinstance(sms, SMSService)               # Check sms is correct type
    print("NotificationFactory test passed")         # Print success message

if __name__ == "__main__":                          # Run tests when file executed
    print("\nRunning basic tests...")               # Print start message
    test_email_service()                            # Run email test
    test_sms_service()                              # Run sms test
    test_factory()                                  # Run factory test
    print("All tests passed successfully!")          # Print final success message

