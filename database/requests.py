# Тут будут запросы в БД
import asyncio
from models import User, async_session
from sqlalchemy import select, update, delete

async  def set_user():
    async with async_session() as session:
        session.add(User(tg_id= 112222, name= "Root"))
        await session.commit()

asyncio.run(set_user())