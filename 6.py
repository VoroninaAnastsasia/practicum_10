def check_message_length(message):
    """Returns the entire message if length < 160, 
    otherwise returns the first 160 characters."""
    return message if len(message) < 160 else message[:160]
