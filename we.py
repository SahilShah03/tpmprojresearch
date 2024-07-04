import random
import string

def generate_key(length):
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=512))
    return key

key = generate_key(16)
print(key)
