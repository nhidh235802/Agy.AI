from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import all_models
from app.api.endpoints import users

# Lệnh này sẽ kiểm tra Database và tạo tất cả bảng nếu chưa có
#Base.metadata.create_all(bind=engine)

app = FastAPI()

# Submit router
app.include_router(users.router, prefix="/api/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Hệ thống Database đã sẵn sàng!"}