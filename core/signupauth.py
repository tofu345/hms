def listToString(s): 
    str = "" 
    for ele in s: 
        str = f"{str}{ele}<br>" 
    return str

def api_listToString(s): 
    str = "" 
    for ele in s: 
        str = f"{str}{ele} " 
    return str

def user_validation(api, username, password, first, last, email):
    special_sym = ['$', '@', '#', '%', '&']
    pswd_errors = []
    val = True

    if username == "" or password == "" or first == "" or last == "" or email == "":
        pswd_errors.append("Please fill all the input fields")
        val = False
    if len(username) < 3:
        pswd_errors.append("Username must be at least 3 characters.")
        val = False
    if len(first) < 3:
        pswd_errors.append("First Name must be at least 3 characters.")
        val = False
    if len(last) < 3:
        pswd_errors.append("Last Name must be at least 3 characters.")
        val = False
    if len(password) < 8:
        pswd_errors.append("Password must be at least 8 characters.")
        val = False
    if len(password) > 20:
        pswd_errors.append("Password length should not exceed 20 characters.")
        val = False
    if not any(char.isdigit() for char in password):
        pswd_errors.append("Password must contain at least one number.")
        val = False
    if not any(char.isupper() for char in password):
        pswd_errors.append("Password must contain at least one uppercase letter.")
        val = False
    if not any(char.islower() for char in password):
        pswd_errors.append("Password must contain at least one lowercase letter.")
        val = False
    if not any(char in special_sym for char in password):
        pswd_errors.append("Password must contain at least one of these symbols $, @, #, %")
        val = False
    
    if api:
        return [val, api_listToString(pswd_errors)]
    else:
        return [val, listToString(pswd_errors)]
