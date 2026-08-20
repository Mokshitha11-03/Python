#18 AUGUST

'''
_username = "mokshitha"
_password = "1234"

successful_attempts = 0
unsuccessful_attempts_U = 0
unsuccessful_attempts_p = 0

def dec1(func):
    def wrap1(*args, **kwargs):
        print("Welcome to our application! Please login to continue.")
        func(*args, **kwargs)
    return wrap1

@dec1
def login(username, password):
    global successful_attempts, unsuccessful_attempts_U, unsuccessful_attempts_p
    if _username == username and _password == password:
        print("Login Successful")
        successful_attempts += 1
    elif username != _username:
        unsuccessful_attempts_U += 1
        if unsuccessful_attempts_U  <= 3:
            username = input("This username doesn't exist. Re-enter the username: ")
            login(username, password)
        else:
            print("You are out of attempts. Try again later.")
            return
    else:
        unsuccessful_attempts_p += 1
        if unsuccessful_attempts_p <= 3:
            password = input("You've entered the wrong password. Re-enter the password: ")
            login(username, password)

login(input("Enter Username:"), input("Enter Password:"))
#login("mokshitha", "1234")
print("Unsuccessful Password Attempts: ", unsuccessful_attempts_p)
print("Unsuccessful Username Attempts: ", unsuccessful_attempts_U)
print("Successful Attempts: ", successful_attempts)
'''

