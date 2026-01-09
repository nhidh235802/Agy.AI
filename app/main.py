from fastapi import FastAPI
from app.core.database import engine, Base
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.models import all_models
from app.api.endpoints import users

# Lệnh này sẽ kiểm tra Database và tạo tất cả bảng nếu chưa có
#Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Submit router
app.include_router(users.router, prefix="/api/users", tags=["Users"])

# 3. Routes cho Frontend (HTML)
# Trang chủ
@app.get("/")
async def read_index():
    return FileResponse("templates/index.html")

# Trang đăng ký
@app.get("/register")
async def read_register():
    return FileResponse("templates/register.html")

# Trang đăng nhập
@app.get("/login")
async def read_login():
    return FileResponse("templates/login.html")