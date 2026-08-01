import sqlite3

DATABASE = "database/lims.db"


def get_connection():
    return sqlite3.connect(DATABASE)
