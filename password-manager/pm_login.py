import hashlib
from pm_encryption_handler import *

with open('User-Data/.user-list.txt', 'a') as fp:
        pass


def make_user(new_name, new_password):
    """
	This function will create a new user and an ecrypted vault for that user

	Args:
        new_name: name of the user
        new_password: password of the user, used for encryption

	Returns:
		None
	"""

    hasher = hashlib.sha3_256()
    bytes_name = bytes(new_name, 'utf-8')
    hasher.update(bytes_name)
    hashed_name = str(hasher.digest())
    bytes_password = bytes(new_password, 'utf-8')
    hasher.update(bytes_password)
    hashed_password = str(hasher.digest())
    
    with open('User-Data/.user-list.txt', 'r') as users_file:
        for user in users_file.readlines():
            credentials = user.split(':')
            if credentials[0] == hashed_name:
                print("Username already in use, please choose a new one")
                return 
    
    with open('User-Data/.user-list.txt', 'a') as users_file:
        user_pass = hashed_name + ':' + hashed_password +'\n'
        users_file.write(user_pass)
    
    vault_name = 'User-Data/.' + new_name + '.txt'
    
    with open(vault_name, 'w') as fp:
        fp.write("Title : Username : Password\n")
        fp.write("...........................\n")
    encrypt_vault(new_name, new_password)
    print("\nUser", new_name, "is succesfully generated and can be logged in to using the credentials given!\n")


def unlock_user(existing_name, master_password):
    """
	This function will check if user exists and an decrypt his vault

	Args:
        new_name: name of the user
        new_password: password of the user, used for encryption

	Returns:
		Tuple containing user credentials
	"""
    hasher = hashlib.sha3_256()
    bytes_name = bytes(existing_name, 'utf-8')
    hasher.update(bytes_name)
    hashed_name = str(hasher.digest())
    bytes_password = bytes(master_password, 'utf-8')
    hasher.update(bytes_password)
    hashed_password = str(hasher.digest())

    with open('User-Data/.user-list.txt', 'r') as users_file:
        users_list = users_file.readlines()
        for u in users_list:
            user_pass = u.split(':')
            if user_pass[0] == hashed_name:
                
                if user_pass[1].strip() == hashed_password:
                    print("Successful login")
                    decrypt_vault(existing_name, master_password)
                    print(existing_name,"'s Vault is Opened.....", sep='')
                    return (existing_name, master_password)
        print("Username or Password is incorrect")