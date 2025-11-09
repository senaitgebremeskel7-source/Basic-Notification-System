
class SMSService:
    """Handles SMS notifications."""

    def __init__(self):
        self.service_type = "SMS"

    def send(self, phone_number, message):
        print(f"Sending SMS to {phone_number}: {message}")
        return True
