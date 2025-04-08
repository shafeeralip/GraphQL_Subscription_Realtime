from schema import schema
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL


graphql_app = GraphQLRouter(schema,subscription_protocols=[GRAPHQL_TRANSPORT_WS_PROTOCOL])

app = FastAPI()
app.include_router(graphql_app,prefix='/graphql')

