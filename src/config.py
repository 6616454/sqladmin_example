from dataclasses import dataclass

from pydantic import BaseSettings


class ConfigExtractor(BaseSettings):
    class Config:
        env_file = '.env'


@dataclass
class Config:
    pass


def load_settings() -> Config:
    config = ConfigExtractor()

    return Config()
