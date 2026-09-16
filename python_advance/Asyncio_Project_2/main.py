import time
import asyncio
import logging
from pathlib import Path
import json
from app import ExternalApiCall

logging.basicConfig(level=logging.DEBUG)


def create_local_db(provided_db: list[dict[str, str | int]]):
    try:
        external_db = provided_db

        if not external_db:
            logging.warning("Api not available")

        base_dir = Path(__file__).parent

        local_db_folder = base_dir / "local_db"

        local_db_folder.mkdir(parents=True, exist_ok=True)

        json_data = local_db_folder / "local_db.json"
        json_data.touch(exist_ok=True)

        with open(json_data, "w", encoding="utf-8") as file:
            json.dump(external_db, file, indent=4)

        logging.info("Local database is created Successfully")

    except Exception as e:
        logging.error(e)


async def main():

    start_time = time.perf_counter()

    external_api = ExternalApiCall()
    api = await external_api.get()


if __name__ == "__main__":
    asyncio.run(main())
