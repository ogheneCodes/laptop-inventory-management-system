from fastapi import FastAPI
import sqlite3

app = FastAPI()

DATABASE = "backend/database/lims.db"


@app.get("/")
def home():
    return {
        "message": "Welcome to Oghenemaga Signature LIMS"
    }


@app.get("/laptops")
def get_laptops():
    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM laptops")

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]
