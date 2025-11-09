# Basic Notification System

A simple and extendable Python notification system using the Factory design pattern.  
Supports multiple notification types such as **Email** and **SMS**.

---
## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Technology Stack](#technology-stack)  
- [Project Structure](#project-structure)  
- [Example Data Model](#example-data-model)  
- [Usage Examples](#usage-examples)  
- [Testing](#testing)  
- [Extending the System](#extending-the-system)  
- [Future Improvements](#future-improvements)
- [License](#license)

## Project Overview

The **Basic Notification System** is a simple and extendable Python application that allows sending notifications via multiple channels, such as **Email** and **SMS**.  

It uses the **Factory Design Pattern** to dynamically create service instances, making it easy to add new notification types without modifying existing code.  

This project is ideal for learning and demonstrating:

- Python class design and object-oriented principles
- Design patterns (Factory Pattern)
- Basic testing of service-oriented code
---

## Features

- Send notifications via **Email** and **SMS**.
- Easily extendable to add new notification services.
- Includes a **factory** for creating service instances dynamically.
- Basic unit tests included.

---
## Technology Stack

- **Programming Language:** Python 3.12 
- **Design Pattern:** Factory Pattern (for creating notification services)   
- **Testing:** Basic unit testing with Python `assert` statements  
---

## Project Structure
```
Basic_Notification_System/
│
├── email_service.py      # Handles email notifications
├── sms_service.py        # Handles SMS notifications
├── factory.py            # NotificationFactory for creating services
├── main.py               # Example usage
├── test_notification.py  # Unit tests for services and factory
└── README.md
 ```
---

## Installation

#### 1. Install Python 3.12.9.
#### 2. Clone the repository:
   ```bash
   git clone https://github.com/senait/Basic-Notification-System.git
   cd Basic_Notification_System
```
#### 3. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

## Example Data Model

The notification system uses simple service classes as the “data model”:

| Class        | Attributes          | Description                        |
|--------------|------------------|------------------------------------|
| EmailService | service_type       | Type of service, e.g., "EMAIL"     |
| SMSService   | service_type       | Type of service, e.g., "SMS"       |
| NotificationFactory | _services     | Registry of available service classes |

Each service class implements a `send(recipient, message)` method to deliver notifications.

## Usage Examples
Running the Main Program

Demonstrates sending notifications via Email and SMS:
```bash
py main.py
```
#### Output:
```pgsql
Sending Email to user@example.com: Hello from Email Service!
Sending SMS to +1234567890: Hello from SMS Service!
All notifications sent successfully!
```

##### Using the Factory Code
```python
from factory import NotificationFactory
from email_service import EmailService
from sms_service import SMSService

factory = NotificationFactory()

# Register notification services
factory.register_service("email", EmailService)
factory.register_service("sms", SMSService)

# Create services dynamically
email = factory.create_service("email")
sms = factory.create_service("sms")

# Send notifications
email.send("user@example.com", "Hello via Email!")
sms.send("+1234567890", "Hello via SMS!")
```
## Testing

Basic unit tests are included in `test_notification.py` to verify functionality:

- **EmailService Test:** Checks sending emails and `service_type` attribute.
- **SMSService Test:** Checks sending SMS and `service_type` attribute.
- **NotificationFactory Test:** Verifies service registration and dynamic creation.


### Running Tests

Run the included tests to verify functionality:

```bash
py test_notification.py
```

Output
```sql
Running basic tests...
Sending Email to test@example.com: Test Email
Sending SMS to +1234567890: Test SMS
NotificationFactory test passed
All tests passed successfully!
```
## Extending the System

To add a new notification type:

##### 1. Create a new service class with a send method.

##### 2. Register it in the factory:
```python
factory.register_service("new_service", NewServiceClass)
```
## Future Improvements

- Add more notification channels (e.g., WhatsApp, Push)  
- Store logs in a database for tracking  
- Implement asynchronous sending and retries  
- Provide a REST API interface  
- Implement robust error handling
---
## License

MIT License © Senait.G
##  Author
Senait G.

📧 Email: senaitG16@gmail.com

🌐 GitHub: github.com/senaitG
