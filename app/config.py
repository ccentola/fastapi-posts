from pydantic import BaseSettings


class Settings(BaseSettings):
    hostname: str
    port: str
    password: str
    username: str
    database: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
