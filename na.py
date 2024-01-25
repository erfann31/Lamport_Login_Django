import hashlib

def _hash_password(password, iterations):
    # Hash the password multiple times using a simple hash function
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for _ in range(iterations - 1):
        hashed_password = hashlib.sha256(hashed_password.encode('utf-8')).hexdigest()
    return hashed_password

def set_password(password):
    hashed_password = _hash_password(password, 1)
    return hashed_password


print(set_password("123"))

