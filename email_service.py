class EmailService:
    """Handles email notifications."""

    def __init__(self):
        self.service_type = "EMAIL"

    def send(self, recipient, message):
        print(f"Sending Email to {recipient}: {message}")
        return True
