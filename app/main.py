from fastapi import FastAPI
from app.routers import user
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()


# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서의 요청을 허용 (배포 시 특정 도메인만 허용하는 것이 보안에 좋습니다)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용 (GET, POST, OPTIONS 등)
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(user.router, prefix="/users", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}