import hashlib

def generate_hash(url: str, length: int):
    url_bytes = url.encode()
    hashed_url = hashlib.sha256(url_bytes).hexdigest()
    return hashed_url[:length]
    
