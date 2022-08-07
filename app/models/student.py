from typing import Optional

from beanie import Document, PydanticObjectId
from pydantic import BaseModel, EmailStr, Field


class Student(Document):
    fullname: str
    email: EmailStr
    course: str
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., gt=0.0, le=4.0)

    class Settings:
        name = "students_collection"


class UpdateStudent(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course: Optional[str]
    year: Optional[int]
    gpa: Optional[float]


class OutStudent(BaseModel):
    id: PydanticObjectId = Field(..., alias="_id")
    fullname: str
    email: EmailStr
    course: str
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., gt=0.0, le=4.0)
