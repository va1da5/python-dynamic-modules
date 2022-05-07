from pydantic import BaseSettings


class Settings(BaseSettings):
    local_dynamic_modules_path: str = "./modules"
    dynamic_modules_path: str = "/tmp/dynamic-modules"


settings = Settings()
