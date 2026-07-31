from schemas import Laptop
from fastapi import FastAPI
from pathlib import Path
import sqlite3

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "database" / "lims.db"


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

@app.post("/laptops")
def create_laptop(laptop: Laptop):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO laptops
        (brand, model, processor, ram, storage, price, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            laptop.brand,
            laptop.model,
            laptop.processor,
            laptop.ram,
            laptop.storage,
            laptop.price,
            laptop.status,
        ),
    )

    conn.commit()

    conn.close()

    return {
        "message": "Laptop added successfully"
    }
