from pydantic import BaseModel, EmailStr
from typing import Optional

# Khuôn mẫu cho dữ liệu người dùng gửi lên để Đăng Ký
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

# Khuôn mẫu cho dữ liệu Server trả về (Không được trả về password!)
class UserResponse(BaseModel):
    id: int
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    tier: str  # free/vip
    
    class Config:
        from_attributes = True # Giúp chuyển đổi từ SQLAlchemy Model sang Pydantic