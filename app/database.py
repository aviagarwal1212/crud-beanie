from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.student import Student

from .config import settings


async def init_db():
    client = AsyncIOMotorClient(f"{settings.database_url}")
    await init_beanie(database=client.students, document_models=[Student])
