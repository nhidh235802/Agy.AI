from passlib.context import CryptContext

# Sử dụng thuật toán bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """Xác minh mật khẩu"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Mã hóa mật khẩu"""
    return pwd_context.hash(password)