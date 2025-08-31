#middleware. for user ip capture..
from user_agents import parse #from the pyaml package
import logging

# Get a logger instance
logger = logging.getLogger("accounts.middleware")

class LogUserIPAddressMiddleware:
    """
    Middleware to log the IP address of the user making the request.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get IP address, accounting for proxies
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        #User logs by pyaml, ua-parser, user-agents
        user_agent_string = request.META.get('HTTP_USER_AGENT', '')
        user_agent = parse(user_agent_string)
        # print(user_agent)
        device_os = user_agent.os.family
        device_browser = user_agent.browser.family
        device_brand = user_agent.device.brand
        device_model = user_agent.device.model
        device_bot = user_agent.is_bot
        device_type = (
            "Smartphone" if user_agent.is_mobile else
            "Tablet" if user_agent.is_tablet else
            "PC" if user_agent.is_pc else
            "other"
        )
        #logic for proxies root and device
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0].strip()
        else:
            ip_address = request.META.get('REMOTE_ADDR', '')

        if request.user.is_authenticated:
            logger.info(f"Logged in user from IP: {ip_address} Device:{device_type} OS: {device_os} Browser: {device_browser} Brand:{device_brand} Model:{device_model} Bot_status:{device_bot}")
        else:
            logger.info(f"Unauthenticated user from IP: {ip_address} Device:{device_type} OS: {device_os} Browser: {device_browser} Brand:{device_brand} Model:{device_model} Bot_status:{device_bot}") 

        response = self.get_response(request)
        return response
