from setup import RABBITMQ
import pika


class RabbitmqConsumer:
  def __init__(self, callback) -> None:
    self.__host = RABBITMQ['host']
    self.__port = int(RABBITMQ['port'])
    self.__username = RABBITMQ['username']
    self.__password = RABBITMQ['password']
    self.__queue = RABBITMQ['queue']
    self.callback = callback
    self.__channel = self.__create_channel()
  
  def __create_channel(self):
    connection_parameters = pika.ConnectionParameters(
    host= self.__host,
    port=self.__port,
    credentials=pika.PlainCredentials(
      username=self.__username,
      password=self.__password
    )
  )
    channel = pika.BlockingConnection(connection_parameters).channel()
    channel.queue_declare(
    queue=self.__queue,
    durable=True
    )
    channel.basic_consume(
    queue=self.__queue,
    auto_ack=True,
    on_message_callback=self.callback
    )

    return channel
  
  def start(self):
    print(f'Listen RabbitMQ on Port 5672')
    self.__channel.start_consuming()

