from typing import Any

import httpx


class ExternalApiCall:

    def __init__(self, url: str):
        self.url = url

    async def get(self, client: httpx.AsyncClient) -> dict[str, Any]:
        response = await client.get(self.url)
        response.raise_for_status()
        return response.json()

    async def create(
        self, client: httpx.AsyncClient, product: dict[str, Any]
    ) -> dict[str, Any]:
        response = await client.post(f"{self.url}/add", json=product)
        response.raise_for_status()
        return response.json()

    async def update(
        self,
        client: httpx.AsyncClient,
        target_id: int,
        product: dict[str, Any],
    ) -> dict[str, Any]:
        self._validate_id(target_id)
        response = await client.put(f"{self.url}/{target_id}", json=product)
        response.raise_for_status()
        return response.json()

    async def delete(self, client: httpx.AsyncClient, target_id: int) -> dict[str, Any]:
        self._validate_id(target_id)
        response = await client.delete(f"{self.url}/{target_id}")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _validate_id(target_id: int) -> None:
        if not isinstance(target_id, int) or target_id <= 0:
            raise ValueError("An id should be a positive integer")
