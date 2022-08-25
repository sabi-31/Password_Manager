import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = '1234567890'
symbols = """~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"""
character_type_default_occurence = {lower: 2, upper: 2, numbers: 2, symbols: 2}

def rand_password():
    """
	This function will return a random string of length requested

	Args:
		No args
	
	Returns:
		string representing random password generated
	"""
    pwd = []
    
    for string, length in character_type_default_occurence.items():
        while length > 0:
            pwd.append(random.choice(string))
            length -= 1
    random.shuffle(pwd)
    return ''.join(pwd)
