import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback-jwt-secret")
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
    ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL")
    RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
    RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "appointment_events")