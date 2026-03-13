import os
import psycopg2
from counter import add_one_to_count, remove_one_to_count

def connect_to_db():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "results"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres")
    )
    return conn


def main():
    conn = connect_to_db()
    cursor = conn.cursor()

    count = add_one_to_count(0)
    print('Affichage du compteur après ajout : ' + str(count))
    cursor.execute(
        "INSERT INTO counter_results (actual_value) VALUES (%s)",
        (count,)
    )
    print('Saved in DB')

    count = remove_one_to_count(50)
    print('Affichage du compteur après retrait : ' + str(count))
    cursor.execute(
        "INSERT INTO counter_results (actual_value) VALUES (%s)",
        (count,)
    )
    print('Saved in DB')

    cursor.execute("SELECT actual_value, updated_at FROM counter_results")
    rows = cursor.fetchall()

    for row in rows:
        print(f"Result: {row[0]} | Date: {row[1]}")

    cursor.close()
    conn.close()

main()

