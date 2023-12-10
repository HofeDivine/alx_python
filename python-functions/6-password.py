def validate_password(password):
    if any(char.isspace() for char in password):
       return False
    elif len(password) >=8 and any(char.isupper() for char in password ) and any(char.islower() for char in password):
        return True
    else:
        return False
    
