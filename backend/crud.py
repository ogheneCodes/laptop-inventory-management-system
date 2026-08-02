import sqlite3
from pathlib import Path

# Absolute path to the database
BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "database" / "lims.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def get_all_laptops():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM laptops")

    rows = cursor.fetchall()

    conn.close()

    laptops = []

    for row in rows:
        laptops.append(
            {
                "id": row["id"],
                "brand": row["brand"],
                "model": row["model"],
                "processor": row["processor"],
                "ram": row["ram"],
                "storage": row["storage"],
                "price": row["price"],
                "status": row["status"],
            }
        )

    return laptops


def get_laptop_by_id(laptop_id: int):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM laptops
        WHERE id = ?
        """,
        (laptop_id,),
    )

    row = cursor.fetchone()

    conn.close()

    return row


def create_laptop(laptop):
    conn = get_connection()

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


def update_laptop(laptop_id: int, laptop):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE laptops
        SET
            brand = ?,
            model = ?,
            processor = ?,
            ram = ?,
            storage = ?,
            price = ?,
            status = ?
        WHERE id = ?
        """,
        (
            laptop.brand,
            laptop.model,
            laptop.processor,
            laptop.ram,
            laptop.storage,
            laptop.price,
            laptop.status,
            laptop_id,
        ),
    )

    conn.commit()

    rows_updated = cursor.rowcount

    conn.close()

    return rows_updated


def delete_laptop(laptop_id: int):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM laptops
        WHERE id = ?
        """,
        (laptop_id,),
    )

    conn.commit()

    rows_deleted = cursor.rowcount

    conn.close()

    return rows_deleted
