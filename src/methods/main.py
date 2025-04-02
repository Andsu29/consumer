from connection.main import Conn
from rabbitmq.consumer import RabbitmqConsumer
from querys.query_post import query_post
import json


class ConsumePublish():
    def __init__(self):
        self.connection = Conn()
        self.rabbitmq_consumer = RabbitmqConsumer(self.minha_callback)

    def minha_callback(self, ch, method, properties, body):
        try:
            with self.connection.create_connection().cursor() as cursor:
                body_str = body.decode("utf-8")
                body_json = json.loads(body_str)
                query = query_post(body_json['titulo'])
                cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            print(f"Erro ao publicar produto: {e}")
        finally:
                self.connection.close_connection()
