from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Mac brew pg，用户名 wangzhe0116，无密码
# 修改这一行！！
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://wangzhe0116@localhost:5432/ai_quality_platform"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
