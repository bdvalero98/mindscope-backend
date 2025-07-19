from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = "super-secret-key"  # reemplaza esto en producción
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
