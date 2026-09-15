import logging
products = [
    {
        "product_id": 1001,
        "name": "Laptop",
        "quantity": 8,
    },
    {
        "product_id": 1002,
        "name": "Keyboard",
        "quantity": 25,
    },
    {
        "product_id": 1003,
        "name": "Mouse",
        "quantity": 3,
    },
]

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

for product in products:
    logging.info("program  Started")

    logging.info(product)

    if product["quantity"] < 10:
        logging.warning(f"{product["product_id"]} have low stock")
    elif not product["product_id"]:
        logging.error(
            "Invalid product data, every product should have valid id")


logging.info("Process completed")
