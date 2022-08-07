import json
from typing import List

from app.models.student import OutStudent, Student, UpdateStudent
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=List[OutStudent])
async def get_students():
    students = await Student.find_all().to_list()
    return students


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutStudent)
async def create_student(student_data: Student):
    student = await Student.insert_one(student_data)
    return student


@router.get("/{id}", response_model=OutStudent)
async def get_student(id: PydanticObjectId):
    student = await Student.get(id)
    if not student:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"student with id {id} not found"
        )
    return student


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(id: PydanticObjectId):
    student = await Student.get(id)
    if not student:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"student with id {id} not found"
        )
    _ = await student.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=OutStudent)
async def update_student(id: PydanticObjectId, student_data: UpdateStudent):
    student = await Student.get(id)
    student_data = jsonable_encoder(student_data)
    if not student:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"student with id {id} not found"
        )
    _ = await student.update({"$set": student_data})
    new_student = await Student.get(id)
    return new_student
