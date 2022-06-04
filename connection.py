import psycopg2
import datetime
from psycopg2 import OperationalError

con = psycopg2.connect(
  database="db_consul",
  user="user_consul",
  password="гыук_сщтыгд1",
  host="rc1b-ilbtnaz6hvc6t2ue.mdb.yandexcloud.net",
  port="6432"
)

def create_connection(host, port, dbname, user, password):
    connection = None
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password,
            target_session_attrs="read-write",
            sslmode="verify-full",
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS requests (
  id SERIAL PRIMARY KEY,
  request TEXT NOT NULL, 
  intents TEXT[],
  date_time TEXT
)
"""

text_arr = ['ртф', 'чемпион']
date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

upload_data = f"""
    INSERT INTO requests (request, intents, date_time)
    VALUES ('хуй', '{text_arr}', '{date_time}')
"""
connection = create_connection("rc1b-ilbtnaz6hvc6t2ue.mdb.yandexcloud.net", 6432, "db_consul", "user_consul", "гыук_сщтыгд1")

execute_query(connection, upload_data)


