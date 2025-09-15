import sqlite3
import os

DEFAULT_DB_PATH = os.path.join('database', 'dataset.db')

def get_connection(db_path: str = DEFAULT_DB_PATH):

    if not os.path.exists(db_path):
        raise FileNotFoundError("DB NOT FOUND!")
    return sqlite3.connect(db_path)

def get_cursor(conn: sqlite3.Connection):
    return conn.cursor()


def save_datasets(df_train, df_val, df_test, mode='detection'):
    conn = get_connection()
    df_train.to_sql(f"train_data_{mode}", conn, if_exists='replace', index=False)
    df_val.to_sql(f"val_data_{mode}", conn, if_exists='replace', index=False)
    df_test.to_sql(f"test_data_{mode}", conn, if_exists='replace', index=False)
    conn.close()
    