from passlib.context import CryptContext
import bcrypt
import hashlib
import base64

def _pre_hash_password(password: str) -> str:
    sha256_hash = hashlib.sha256(password.encode('utf-8')).digest()
    return base64.b64encode(sha256_hash).decode('utf-8')

def get_password_hash(password: str) -> str:
    # 1. Băm sơ bằng SHA-256 để rút gọn mật khẩu về độ dài cố định (< 72 bytes)
    pre_hashed = _pre_hash_password(password)
    
    # 2. Tạo muối (salt) và băm bằng Bcrypt
    salt = bcrypt.gensalt(rounds=12) # rounds=12 là độ khó tiêu chuẩn hiện nay
    hashed = bcrypt.hashpw(pre_hashed.encode('utf-8'), salt)
    
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    pre_hashed = _pre_hash_password(plain_password)
    return bcrypt.checkpw(
        pre_hashed.encode('utf-8'), 
        hashed_password.encode('utf-8')
    )