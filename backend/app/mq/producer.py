import json
import pika
from config import Config


def publish_appointment_event(payload):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=Config.RABBITMQ_HOST)
    )
    channel = connection.channel()
    channel.queue_declare(queue=Config.RABBITMQ_QUEUE, durable=True)

    channel.basic_publish(
        exchange="",
        routing_key=Config.RABBITMQ_QUEUE,
        body=json.dumps(payload),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    connection.close()