import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """
    This class represents the project level settings.
    """
    
    # QA Link
    HOST: str = os.getenv('APP_HOSTNAME')

    # QA Password
    HOST_PASSWORD: str = os.getenv("APP_PASSWORD") 
