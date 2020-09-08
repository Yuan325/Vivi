from config import config
import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        return conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



def databaseExecute(cur, query):
    print('PostgreSQL database version:')
    cur.execute(query)
    data = cur.fetchone()
    print(data)