class NotificationFactory:
    """A simple and extendable factory for notification services."""

    def __init__(self):
        # Register services here
        self._services = {}

    def register_service(self, name, service_class):
        """Register a new service with the factory."""
        self._services[name.lower()] = service_class

    def create_service(self, service_type):
        """Create a service instance based on the type."""
        service_class = self._services.get(service_type.lower())
        if not service_class:
            raise ValueError(f"Unknown service type: {service_type}")
        return service_class()
