from email_service import EmailService
from sms_service import SMSService
from factory import NotificationFactory

def test_email_service():
    service = EmailService()
    result = service.send("test@example.com", "Test Email")
    assert result is True
    assert service.service_type == "EMAIL"

def test_sms_service():
    service = SMSService()
    result = service.send("+1234567890", "Test SMS")
    assert result is True
    assert service.service_type == "SMS"

def test_factory():
    factory = NotificationFactory()
    # Register services
    factory.register_service("email", EmailService)
    factory.register_service("sms", SMSService)

    email = factory.create_service("email")
    sms = factory.create_service("sms")

    assert isinstance(email, EmailService)
    assert isinstance(sms, SMSService)
    print("NotificationFactory test passed")

if __name__ == "__main__":
    print("\nRunning basic tests...")
    test_email_service()
    test_sms_service()
    test_factory()
    print("All tests passed successfully!")
