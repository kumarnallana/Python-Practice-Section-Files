from app import FetchExternalApi
import json
from pathlib import Path
import asyncio

import time 

class CreateJson():
    def create_json(self,provided_db:list[dict[str: str | int]]):
        try:
            
            if not provided_db:
                return None

            base_dir = Path(__file__).parent
            local_db = base_dir / "data"
            local_db.mkdir(parents=True, exist_ok=True)
            json_file = local_db / "album.json"
            json_file.touch(exist_ok=True)

            with open(json_file, "w", encoding="utf-8") as file:
                json.dump(provided_db, file, indent=4)

        except Exception as e:
            return f"Error: {e}"


async def main():

    try:
        start_time = time.perf_counter()

        external_api = FetchExternalApi()

        api = await external_api.api_response()

        create_json_db = CreateJson()

        database = create_json_db.create_json(api)

        end_time = time.perf_counter()

        total_time = end_time - start_time

        return f"Total Taken time to execute albums api: {total_time:.2f}"

    except Exception as e:
        return f"Error: {e}"



if __name__ == "__main__":
    print(asyncio.run(main()))