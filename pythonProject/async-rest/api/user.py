from fastapi import APIRouter, Depends, HTTPException
from dependencies.session import get_db_session
from services.user import UserService

router_user = APIRouter(prefix="/user/", tags=["用户API"])


@router_user.get('/{user_id}')
async def get_user(userid: int, db_session=Depends(get_db_session())):
    query_user = await UserService.get_user(db_session, userid)
    return {'code': 200, 'msg': 'success', 'data': {'user': query_user}}
