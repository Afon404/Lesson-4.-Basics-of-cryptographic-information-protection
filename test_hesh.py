import hashlib
hash_object = hashlib.sha256(b'test')
print(hash_object.hexdigest())