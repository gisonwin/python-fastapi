from fastapi import APIRouter

course_api = APIRouter()


@course_api.get('/')
async def get_course():
    return {
        "data": "查看所有的课程"
    }


@course_api.post('/')
async def post_course():
    return {
        "data": "添加一个课程"
    }


@course_api.get('/{cid}')
async def get_one_course(cid: int):
    return {
        "data": f"查看一个id={cid}的课程"
    }


@course_api.put('/{cid}')
async def update_one_course(cid: int):
    return {
        "data": f"更新一个id={cid}的课程"
    }


@course_api.delete('/{cid}')
async def delete_one_course(cid: int):
    return {
        "data": f"删除一个id={cid}的课程"
    }
