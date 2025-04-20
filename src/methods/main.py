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

                query = query_post(
                     body_json['titulo'], body_json['descricao'], body_json['preco'], body_json['categoria'], body_json['marca'], body_json['modelo'], body_json['codpro'], body_json['id'], body_json['cor'])
                
                cursor.execute(query)
                self.connection.commit()
                ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Erro ao publicar produto: {e}")
        finally:
                self.connection.close_connection()
