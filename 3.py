import asyncio
import random
from typing import List


class SharedState:
    items: List[int]

    def __init__(self):
        self.items = []

    async def modify(self, value: int):
        await asyncio.sleep(random.randint(1, 2))
        self.items.append(value)


class Server:
    state: SharedState

    def __init__(self, state: SharedState, semaphore: asyncio.Semaphore):
        self.state = state
        self.semaphore = semaphore

    async def handle_request(self, value: int):
        async with self.semaphore:
            await self.state.modify(value)


async def main():
    state = SharedState()
    semaphore = asyncio.Semaphore(1)  # Ограничиваем количество одновременных запросов до 1
    server = Server(state, semaphore)

    # Имитируем запуск 10 запросов к серверу
    requests = [server.handle_request(value) for value in range(10)]
    await asyncio.gather(*requests)

    print(state.items == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    for item in state.items:
        print(item)


if __name__ == '__main__':
    asyncio.run(main())