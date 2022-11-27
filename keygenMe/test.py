import hashlib

hash = hashlib.sha256(b"FRASER").hexdigest()

print(hash)

hashed = "92d7ac3c9a0cf9d527a5906540d6c59c80bf8d7ad5bb1885f5f79b5b24a6d387"

key = hashed[4] + hashed[5] + hashed[3] + hashed[6] + hashed[2] + hashed[7] + hashed[1] + hashed[8] 

print(key)
