import asyncio


class ApiManager:

    async def get_users(self, data: list[str]):
        print("⏳ [Users] Fetching users (takes 3s)...")
        await asyncio.sleep(3)
        print("✅ [Users] Fetched successfully!")
        return f"{len(data)} Users fetched"

    async def get_products(self, data: list[str]):
        print("⏳ [Products] Fetching products (takes 7s)...")
        await asyncio.sleep(7)
        print("✅ [Products] Fetched successfully!")
        return f"{len(data)} Products fetched"

    async def get_orders(self, data: list[int]):

        print("⏳ [Orders] Fetching orders (takes 1s)...")

        await asyncio.sleep(1)
        print("✅ [Orders] Fetched successfully!")
        return f"{len(data)} Orders fetched"
