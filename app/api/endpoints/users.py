from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.all_models import User, UserTier
from app.schemas.user_schema import UserCreate, UserResponse
from app.core.security import get_password_hash

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # 1. Kiểm tra xem email đã tồn tại chưa
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400, 
            detail="Email này đã được đăng ký rồi!"
        )
    
    # 2. Mã hóa mật khẩu
    hashed_pwd = get_password_hash(user_data.password)
    
    # 3. Tạo User mới (Mặc định là Free Tier)
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_pwd,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        tier=UserTier.FREE
    )
    
    # 4. Lưu vào Database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user