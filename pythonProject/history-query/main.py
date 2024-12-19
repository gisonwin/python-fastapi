# coding=utf-8
import uvicorn
from fastapi import FastAPI
import fastapi_cdn_host

from settings import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise
from api.student import student_api
from api.course import course_api

app = FastAPI()
fastapi_cdn_host.patch_docs(app)
register_tortoise(
    app,
    config=TORTOISE_ORM
)

app.include_router(student_api, prefix="/student", tags=["选课系统的学生接口"])
app.include_router(course_api, prefix="/course", tags=["选课系统的课程接口"])


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)
