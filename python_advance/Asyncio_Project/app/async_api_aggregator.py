import httpx


class FetchExternalApi:
    async def fetch_json(self, client: httpx.AsyncClient, url: str):
        try:
            response = await client.get(url)

            response.raise_for_status()

            return response.json()

        except Exception as e:
            return f"Error: {e}"

    async def api_response(self):
      try:
          async with httpx.AsyncClient(timeout=10.02) as client:

            json_data = await self.fetch_json(client, "https://jsonplaceholder.typicode.com/photos")

            return json_data
            
      except Exception as e:
        return f"Error: {e}"
        