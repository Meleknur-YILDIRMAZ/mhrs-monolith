from pymongo import MongoClient
from config import Config

sample_hospitals = [
    {
        "city": "Kütahya",
        "hospital": "Kütahya Şehir Hastanesi",
        "department": "Kardiyoloji",
        "doctor": "Dr. Ahmet Yılmaz"
    },
    {
        "city": "Kütahya",
        "hospital": "Kütahya Devlet Hastanesi",
        "department": "Dahiliye",
        "doctor": "Dr. Elif Kaya"
    },
    {
        "city": "Eskişehir",
        "hospital": "Eskişehir Şehir Hastanesi",
        "department": "Göz Hastalıkları",
        "doctor": "Dr. Mehmet Demir"
    }
]

client = MongoClient(Config.MONGO_URI)
db = client[Config.MONGO_DB_NAME]

if db.hospitals.count_documents({}) == 0:
    db.hospitals.insert_many(sample_hospitals)
    print("Seed verileri eklendi")
else:
    print("Seed zaten mevcut")