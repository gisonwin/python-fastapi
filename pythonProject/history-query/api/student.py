from fastapi import APIRouter

from model.models import Student

student_api = APIRouter()


@student_api.get('/')
async def get_student():
    # 查询所有
    # students = await Student.all()
    # print(students)

    # 查询过滤 filter 返回 queryset
    # students = await Student.filter(clazz_id=2)
    # for student in students:
    #     print(student.name, student.sno)
    # 查询过滤 get 返回单体对象
    # stu = await Student.get_or_none(id=1)
    # if stu:
    #     print(stu.name)
    # else:
    #     print(f"student id={id} not found")
    # 模糊查询  id大于1 gt  、大于等于 gte / id in [1,2] id=1 or id=2 / range [1,1000)
    # students = await Student.filter(sno__gt=2001)
    # students = await Student.filter(sno__in=[1,2])
    # students = await Student.filter(sno__range=[2000,3000])
    # for student in students:
    #     print(student.name, student.id, student.sno)
    #   模糊查询 values 返回字典
    # students = await Student.filter(sno__gt=2001)
    students = await Student.all().values("name", "sno")
    print(students)

    return {
        "查看所有的学生": students,
    }


@student_api.get("/index.html")
async def get_index():
    students = await Student.all()

    return students


@student_api.post('/')
async def post_student():
    return {
        "data": f"添加一个学生"
    }


@student_api.get('/{sid}')
async def get_one_student(sid: int):
    stu = await Student.get_or_none(id=sid)
    if stu:
        return {
            "data": f"查看一个id={sid}的学生"
        }
    else:
        print(f"没有找到id={sid}的学生")


@student_api.put('/{sid}')
async def update_one_student(sid: int):
    return {
        "data": f"更新一个id={sid}的学生"
    }


@student_api.delete('/{sid}')
async def delete_one_student(sid: int):
    return {
        "data": f"删除一个id={sid}的学生"
    }
