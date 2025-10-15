from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://taskforge_user:taskforge_pass@db:5432/taskforge_db"

    class Config:
        env_file = ".env"

settings = Settings()
