import string
from random import *
chars = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(chars)for x in range(randint(8,16)))
print (password)