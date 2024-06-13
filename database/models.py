# Тут  создана модель (тк ООП) или структура БД
import asyncio
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3', echo= True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(25))
    sell_buy: Mapped[int] = mapped_column
    selling_name: Mapped[str] = mapped_column(String(50))
    year: Mapped[int] = mapped_column
    has_documents: Mapped[str] = mapped_column(String(25))
    engine_type: Mapped[str] = mapped_column(String(25))
    working_width: Mapped[str] = mapped_column(String(25))
    condition: Mapped[str] = mapped_column(String(25))
    inspection_location: Mapped[str] = mapped_column(String(50))
    payment_method: Mapped[str] = mapped_column(String(50))
    company_details: Mapped[str] = mapped_column(String(50))
    self_loading: Mapped[str] = mapped_column(String(50))
    photos_and_video: Mapped[str] = mapped_column(String(50))
    commission_rate: Mapped[str] = mapped_column(String(50))
    phone : Mapped[str] = mapped_column(String(15))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
