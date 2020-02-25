import string
from random import *
chars = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(chars)for x in range(int(input('Enter the length of your password'))))
print (password)