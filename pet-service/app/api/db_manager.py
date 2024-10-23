from app.api.models import PetIn, PetOut
from app.api.db import pets, database
from typing import Optional


async def add_pet(payload: PetIn, pet_id: str):
    query = pets.insert().values(id=pet_id, **payload.model_dump())

    return await database.execute(query=query)


async def get_all_pets(
    type: Optional[str], limit: Optional[int], offset: Optional[int]
):
    query = pets.select()

    if type is not None:
        query = query.where(pets.c.type == type)

    if limit is not None:
        query = query.limit(limit)

    if offset is not None:
        query = query.offset(offset)

    return await database.fetch_all(query)


async def get_pet(id):
    query = pets.select().where(pets.c.id == id)
    return await database.fetch_one(query=query)


async def update_pet(id: int, payload: PetIn):
    query = pets.update().where(pets.c.id == id).values(**payload.model_dump())
    return await database.execute(query=query)


async def delete_pet(id: int):
    query = pets.delete().where(pets.c.id == id)
    return await database.execute(query=query)


async def delete_all_pets():
    query = pets.delete()
    return await database.execute(query=query)