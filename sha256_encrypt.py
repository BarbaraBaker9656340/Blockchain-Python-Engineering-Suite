import hashlib

def sha256_encrypt(data: str) -> str:
    if not isinstance(data, str):
        data = str(data)
    hash_obj = hashlib.sha256(data.encode('utf-8'))
    return hash_obj.hexdigest()

def verify_data_hash(original_data: str, target_hash: str) -> bool:
    return sha256_encrypt(original_data) == target_hash
