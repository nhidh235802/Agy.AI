from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import all_models

# Lệnh này sẽ kiểm tra Database và tạo tất cả bảng nếu chưa có
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hệ thống Database đã sẵn sàng!"}