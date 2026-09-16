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

    def create_local_db(self):
        try:

            external_db = self.get()

            if not external_db:
                logging.warning("Api not available")

            base_dir = Path(__file__).parent

            local_db_folder = base_dir / "local_db"

            local_db_folder.mkdir(parents=True, exist_ok=True)

            json_data = local_db_folder / "local_db.json"
            json_data.touch(exist_ok=True)

            with open(json_data, "w", encoding="utf-8") as file:
                json.dump(external_db, file, indent=4)

        except Exception as e:
            logging.error(e)


external_api_call = ExternalApiCall()
