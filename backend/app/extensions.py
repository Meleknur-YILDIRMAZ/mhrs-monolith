from flask_jwt_extended import JWTManager
from flask_cors import CORS
from pymongo import MongoClient
from elasticsearch import Elasticsearch

jwt = JWTManager()
cors = CORS()

mongo_client = None
db = None
es = None


def init_database(app):
    global mongo_client, db
    mongo_client = MongoClient(app.config["MONGO_URI"])
    db = mongo_client[app.config["MONGO_DB_NAME"]]


def init_elasticsearch(app):
    global es
    es = Elasticsearch(app.config["ELASTICSEARCH_URL"])


def get_db():
    return db


def get_es():
    return es