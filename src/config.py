from dataclasses import dataclass

from pydantic import BaseSettings

from src.infrastructure.db.config import DBConfig
from src.presentation.api.config import APIConfig


class ConfigExtractor(BaseSettings):
    title: str
    database_url: str

    class Config:
        env_file = '.env'


@dataclass
class Config:
    api: APIConfig
    db: DBConfig


def load_config() -> Config:
    config = ConfigExtractor()

    return Config(
        api=APIConfig(
            title=config.title
        ),
        db=DBConfig(
            database_url=config.database_url
        )
    )
