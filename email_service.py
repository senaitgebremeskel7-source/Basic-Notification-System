class EmailService:                # Class for email notifications
    """Handles email notifications."""  # Description of the class

    def __init__(self):            # Constructor
        self.service_type = "EMAIL"  # Set service type

    def send(self, recipient, message):  # Method to send email
        print(f"Sending Email to {recipient}: {message}")  # Print sending message
        return True                  # Return True if sent
