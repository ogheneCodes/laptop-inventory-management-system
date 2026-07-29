# Laptop Inventory Management System Database Design

## Purpose

The database stores and manages information required for laptop inventory, customers, and sales operations.

---

# Tables

## Laptops Table

Stores laptop information.

Fields:

- id
- brand
- model
- processor
- ram
- storage
- purchase_price
- selling_price
- status

---

## Customers Table

Stores customer information.

Fields:

- id
- name
- phone
- email

---

## Sales Table

Stores completed transactions.

Fields:

- id
- laptop_id
- customer_id
- date
- amount

---

# Relationships

Customers can purchase laptops.

Sales records connect customers and laptops.
