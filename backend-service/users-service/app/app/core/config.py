import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "Users Service"
    PROJECT_DESCRIPTION: str = "Users service API documentation"
    API_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "dev"
    POSTGRES_PASSWORD: str = "dev"
    POSTGRES_DB: str = "users"
    SQLALCHEMY_DATABASE_URI: Optional[
        PostgresDsn
    ] = "postgresql://dev:dev@localhost:54322/users"

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = "admin@admin.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin"
    FIRST_NAME_SUPERUSER: str = "admin"
    LAST_NAME_SUPERUSER: str = "admin"
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True


settings = Settings()
