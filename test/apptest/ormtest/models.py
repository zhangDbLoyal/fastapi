from tortoise.models import Model
from tortoise import fields

class Student (Model):
    id = fields.IntField(pk=True,description="id")
    name = fields.CharField(max_length=20,description="学生名称")
    age = fields.IntField(description="年龄")

    clas = fields.ForeignKeyField("Clas",related_name="students")
    teacher = fields.ForeignKeyField("Teacher",related_name="students")
    course = fields.ManyToManyField("Course",related_name="students",)
class Clas (Model):
    id = fields.IntField(pk=True,description="id")
    name = fields.CharField(max_length=20,description="班级名称")

class Course (Model):
    id = fields.IntField(pk=True,description="id")
    name = fields.CharField(max_length=20,description="课程名称")

class Teacher (Model):
    id = fields.IntField(pk=True,description="id")
    name = fields.CharField(max_length=20,description="教师名称")
    age = fields.IntField(description="年龄")
