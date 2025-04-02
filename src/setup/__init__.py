import os
import dotenv


dotenv.load_dotenv()

DB2 = {     
        "host": os.environ['DB_HOST'],
        "user": os.environ['MYSQL_USER'],
        "password": os.environ['MYSQL_PASSWORD'],
        "database": os.environ['MYSQL_DATABASE'],
        "port": os.environ['DB_PORT']
}

RABBITMQ = {     
        "host": os.environ['RABBITMQ_HOST'],
        "username": os.environ['RABBITMQ_USER'],
        "password": os.environ['RABBITMQ_PASS'],
        "queue": os.environ['RABBITMQ_QUEUE'],
        "port": os.environ['RABBITMQ_PORT']
}