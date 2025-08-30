# In your middleware.py
import logging

# Get a logger instance
logger = logging.getLogger(__name__)

class LogUserIPAddressMiddleware:
    """
    Middleware to log the IP address of the user making the request.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the user's IP address (handling proxies if any)
        ip_address = request.META.get('REMOTE_ADDR')
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]
        
        # Log the user's IP address at the INFO level
        logger.info(f"User IP address: {ip_address}")

        # Proceed with the request
        response = self.get_response(request)

        return response
