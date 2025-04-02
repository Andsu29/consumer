from decorators.get_exception import get_exception
from methods.main import ConsumePublish


@get_exception
def main():
    consume_publish = ConsumePublish()
    print("Iniciando consumidor")
    consume_publish.rabbitmq_consumer.start()
    print("Serviço finalizado")
