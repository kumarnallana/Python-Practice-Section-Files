import httpx
import json
from pathlib import Path
import logging


class ExternalApiCall:

    logging.basicConfig(level=logging.DEBUG)

    async def fetch(self, client: httpx.AsyncClient, url: str):
        response = await client.get(url)

        response.raise_for_status()

        return response.json()

    async def get(self):
        async with httpx.AsyncClient(timeout=10.05) as client:

            external_db = await self.fetch(client, "https://dummyjson.com/products")

            return external_db


logging.info("Local database is created Successfully")
