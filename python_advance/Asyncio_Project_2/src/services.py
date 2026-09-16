import httpx
import json
from pathlib import Path


class ExternalApiCall:
    async def fetch(self, client: httpx.AsyncClient, url: str):
        response = await client.get(url)

        response.raise_for_status()

        return response.json()

    async def get(self):
        async with httpx.AsyncClient as client:

            external_db = await self.fetch(client, "https://dummyjson.com/products")

            return external_db

    def create_local_db(self):

        external_db = self.get()

        base_dir =
