from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "DevOps Platform API"
    debug: bool = False
    database_url: str = "sqlite:///./app.db"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
