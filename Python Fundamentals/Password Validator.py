def password_chek(some_password):
    password_validation = True
    if len(some_password) < 6 or len(some_password) > 10 :
        print('Password must be between 6 and 10 characters')
        password_validation = False
    if not some_password.isalnum():
        print('Password must consist only of letters and digits')
        password_validation = False
    digits_counter = 0
    for character in some_password:
        if character.isdigit():
            digits_counter +=1
    if digits_counter < 2:
        print("Password must have at least 2 digits")
        password_validation = False
    return password_validation

password = input()
password_is_valid = password_chek(password)
if password_is_valid:
    print('Password is valid')