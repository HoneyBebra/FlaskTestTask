from dotenv import load_dotenv
import os


load_dotenv()
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
host = os.getenv('HOST')
port = os.getenv('PORT')

ENGINE_URL = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
SQLALCHEMY_ECHO = False

FLASK_DEBUG = True
