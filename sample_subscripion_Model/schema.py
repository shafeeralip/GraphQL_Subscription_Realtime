import asyncio
import strawberry
from typing import AsyncGenerator



message_queue = asyncio.Queue()


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello world"

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def messages(self) -> AsyncGenerator[str, None]:
        while True:
            message = await message_queue.get()
            yield message

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def send_message(self, msg: str) -> str:
        await message_queue.put(msg)
        return "Message sent"
    

schema = strawberry.Schema(query=Query,mutation=Mutation,subscription=Subscription)