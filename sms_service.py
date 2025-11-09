class SMSService:                              # Class for SMS notifications
    """Handles SMS notifications."""           # Description of the class

    def __init__(self):                        # Constructor
        self.service_type = "SMS"              # Set service type

    def send(self, phone_number, message):     # Method to send SMS
        print(f"Sending SMS to {phone_number}: {message}")  # Simulate sending SMS
        return True                            # Return True if sent
