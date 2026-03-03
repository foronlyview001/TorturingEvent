"""
User management module
"""
import state

users = []

def add_user():
    """Add a new user"""
    # BUG 9 FIXED: Use the function from state module to ensure global update
    state.increment_count()
    
    user_id = len(users) + 1
    users.append(f"User_{user_id}")
    
    # BUG 8 FIXED: Local import to break circular dependency
    from module_b import log_analytics
    log_analytics("user_added", user_id)
    
    return user_id

def get_user_list():
    """Get list of all users"""
    return users

def remove_user(user_id):
    """Remove a user"""
    if 0 < user_id <= len(users):
        users.pop(user_id - 1)
      
