def alphanumeric(password: str) -> bool:
    
    if password == "":
        return False
    
    for ch in password:
        if not(ch.isalpha() or ch.isnumeric()):
            return False
    
    return True