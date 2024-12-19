from fastapi import APIRouter, Request, Response

paramRouter = APIRouter()


@paramRouter.get('/param/')
async def get_param(request: Request):
    print(
        f"request:{request.url},host:{request.client.host},headers:{request.headers},{request.body},cookies:{request.cookies}")
    return Response
