from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    sha = hashlib.sha256(password.encode("utf-8")).digest()
    return pwd_context.hash(sha)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    sha = hashlib.sha256(plain_password.encode("utf-8")).digest()
    return pwd_context.verify(sha, hashed_password)
