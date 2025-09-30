import psycopg2 as pg 
from dotenv import load_dotenv
import os

load_dotenv()

params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_HOST"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}

