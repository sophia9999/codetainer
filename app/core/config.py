from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

ENV = os.getenv("ENV", "local")
ENV_FILE = f".env.{ENV}"

if os.path.exists(ENV_FILE):
    print(f"Loading environment file: {ENV_FILE}")
    # 서버 세팅 시 error 사항 때문에 추가 
    # .env에서 불러온 변수는 os.getenv()에서만 사용할 수 있고 os.environ에는 자동 반영되지 않으므로 내부에서 환경 변수 등록 시 에로 사항이 있어 등록을 위함
    load_dotenv(ENV_FILE, override=True)
else:
    print(f"Warning: `{ENV_FILE}` file not found. Using default settings.")


class Settings(BaseSettings):
    ENV: str = "dev"
    LOG_DIR: str = "./logs"
    
    UVICORN_HOST: str = "127.0.0.1"
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool 
    DEBUG: bool = ENV != "prod"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=True
    )

# 인스턴스화
settings = Settings()