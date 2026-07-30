from fastapi import FastAPI

app = FastAPI()

# Mock inventory data
laptops = [
    {
        "id": 1,
        "brand": "HP",
        "model": "EliteBook 840 G8",
        "processor": "Intel Core i5",
        "ram": "16GB",
        "storage": "512GB SSD",
        "price": 350000,
        "status": "In Stock"
    },
    {
        "id": 2,
        "brand": "Dell",
        "model": "Latitude 5420",
        "processor": "Intel Core i5",
        "ram": "8GB",
        "storage": "256GB SSD",
        "price": 280000,
        "status": "Sold",
    },


{
	"id": 3,
        "brand": "Lenovo",
        "model": "ThinkPad T14",
        "processor": "Intel Core i5",
        "ram": "16GB",
        "storage": "1TB SSD",
        "price": 300000,
        "status": "Available",
},

]


@app.get("/")
def home():
    return {
        "Welcome to Oghenemaga Signature LIMS"
    }


@app.get("/laptops")
def get_laptops():
    return laptops
