from fastapi import APIRouter, Request, Depends, Response, HTTPException

commandRouter = APIRouter()


@commandRouter.get("/command/")
async def get_command(request: Request,response: Response):
    return Response("Hello World")
