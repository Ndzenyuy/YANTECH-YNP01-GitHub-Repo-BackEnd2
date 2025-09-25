import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    # AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    # AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID", "975391191374")
    APP_CONFIG_TABLE = os.getenv("APP_CONFIG_TABLE", "YANTECH-YNP01-AWS-appTable-dev")

settings = Settings()

