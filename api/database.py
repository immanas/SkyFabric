import psycopg2

def get_db_connection():
    return psycopg2.connect(
        dbname="skyfabric",
        user="postgres",
        password="Manas@123",
        host="localhost",
        port="5433"
    )
