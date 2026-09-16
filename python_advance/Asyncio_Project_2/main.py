import asyncio
import json
import logging
import time
from pathlib import Path
from typing import Any

import httpx
from app import ExternalApiCall

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def save_local_db(products: dict[str, Any]) -> None:
    database_path = Path(__file__).parent / "local_db" / "local_db.json"
    database_path.parent.mkdir(parents=True, exist_ok=True)

    with database_path.open("w", encoding="utf-8") as file:
        json.dump(products, file, indent=4)

    logging.info("Local database saved to %s", database_path)


async def main():
    new_product = {
        "title": "Essence Mascara Lash Princess",
        "description": "A popular volumizing and lengthening mascara.",
        "category": "beauty",
        "price": 9.99,
    }
    start_time = time.perf_counter()

    async with httpx.AsyncClient(timeout=10.05) as client:
        products_api = ExternalApiCall("https://dummyjson.com/products")
        products = await products_api.get(client)
        save_local_db(products)

        created_product = await products_api.create(client, new_product)
        logging.info("Created product with id %s", created_product.get("id"))

    logging.info("Execution time: %.4f seconds",
                 time.perf_counter() - start_time)


if __name__ == "__main__":
    asyncio.run(main())
