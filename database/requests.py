import asyncio
from database.models import User, async_session
from sqlalchemy import select, update, delete


async def set_user(tg_id: int = 0, name= "None", phone = "None", sell_buy = 0, selling_name = "None"):
    async with async_session() as session:
        # user = await session.scalar(select(User).where(User.tg_id == tg_id))

        # if not user:
        session.add(User(tg_id=tg_id, name=name,phone=phone,sell_buy=sell_buy,selling_name=selling_name ))
        await session.commit()


async def f_user(data, tg_id:int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user.tg_id == tg_id:
            user.selling_name =data['selling_name']

            await session.commit()
        #
        #     session.add(user.selling_name= data['selling_name'])
        #     # session.add(User(tg_id=tg_id, name=data['name'], phone=data['phone'], sell_buy=data['sell_buy'], selling_name=data['selling_name']))
        #
        #     # user.salling_name= data['selling_name']
        #     await session.commit()



