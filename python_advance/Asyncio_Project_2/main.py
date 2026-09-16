import asyncio
import logging
from pathlib import Path
import json
from app import ExternalApiCall

logging.basicConfig(level=logging.DEBUG)


async def create_local_db(self):
    try:

        external_db = ExternalApiCall()

        external_db = await self.get()

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

if __name__ == "__main__":
    asyncio.run(create_local_db())
