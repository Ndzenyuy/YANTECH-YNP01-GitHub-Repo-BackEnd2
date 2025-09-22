import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL", "https://sqs.us-east-1.amazonaws.com/975391191374/YANTECH-YNP01-AWS-sqs-notification-requests-dev")
APPLICATIONS_TABLE = os.getenv("APPLICATIONS_TABLE")
REQUEST_LOG_TABLE = os.getenv("REQUEST_LOG_TABLE")

