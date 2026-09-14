import time
from async_task_simulator import ApiManager
import asyncio
from data import products, orders, users


async def main():

    api_manager = ApiManager()

    start_time = time.perf_counter()

    await asyncio.gather(
        api_manager.get_users(users),
        api_manager.get_products(products),
        api_manager.get_orders(orders)
    )

    end_time = time.perf_counter()

    total_time = end_time - start_time

    print(f"Total Execution time : {total_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
