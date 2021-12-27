import psycopg2
from psycopg2 import Error


def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="Lab_2",
        user="postgres",
        password="23032002")
    return conn


def statistics(conn):
    cursor = conn.cursor()

    try:
        cursor.execute("""
        SELECT winner, count(*)
        FROM public.games
        GROUP BY winner;
        """)

        records = cursor.fetchall()
        print(f"Counts of winners: {records}")

        cursor.execute("""
        SELECT rated, count(*)
        FROM public.games
        GROUP BY rated;
        """)

        records = cursor.fetchall()
        print(f"Were games rate? {records}")

        cursor.execute("""
                SELECT game_status, count(*)
                FROM public.games
                GROUP BY game_status;
                """)

        records = cursor.fetchall()
        print(f"Counts of end game types: {records}")
	cursor.close()
    except (Exception, Error) as e:
        print(e)


if __name__ == '__main__':
    conn = get_connection()
    statistics(conn)
    conn.close()
