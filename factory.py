class NotificationFactory:                          # Class to create notification services
    """A simple and extendable factory for notification services."""  # Description of the class

    def __init__(self):                              # Constructor
        self._services = {}                          # Dictionary to store registered services

    def register_service(self, name, service_class): # Register a new service
        self._services[name.lower()] = service_class # Add service to dictionary

    def create_service(self, service_type):           # Create service instance
        service_class = self._services.get(service_type.lower())  # Get service class by name
        if not service_class:                         # If service not found
            raise ValueError(f"Unknown service type: {service_type}")  # Raise error
        return service_class()                        # Return new service instance
