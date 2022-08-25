import os
path = 'User-Data'

try:
    os.mkdir(path)
except OSError:
    pass


def save_to_file(existing_name, master_password, t, u, p):
    """
	This function will save login credentials to the user's file

	Args:
        existing_name: name of the user
        master_password: user's main password
		t: Title of the login credential to be saved
        u: Username
        p: Password
	
	Returns:
		None
	"""
    vault_name = 'User-Data/.' + existing_name + '.txt'
    with open(vault_name, 'a') as vault:
        credential = t + ':' + u + ':' + p + '\n'
        vault.write(credential)


def print_vault(existing_name):
    """
	This function will print login credentials from the user's file

	Args:
        existing_name: name of the user
        
	Returns:
		None
	"""
    vault_name = 'User-Data/.' + existing_name + '.txt'
    
    with open(vault_name, 'r') as vault:
        for line in vault.readlines():
            print(line)