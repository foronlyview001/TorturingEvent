"""
Utility functions
"""
from config import MAX_USERS

def calculate_capacity(current, maximum):
    """
    BUG 5 FIXED: Returns True when current < maximum (has room)
    """
    return current < maximum

def validate_user_id(user_id):
    """Validate user ID is positive"""
    return user_id > 0

def get_max_capacity():
    """Return maximum capacity"""
    return MAX_USERS

# BUG 6 FIXED: Removed division by zero
def hidden_bonus_calculator(x):
    """Unused function with critical bug fixed"""
    return x / 1 if x != 0 else 0

def inefficient_function(data):
    """Cleaned up implementation"""
    return [val for i, val in enumerate(data)]
  
