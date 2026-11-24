from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings

# Create async database engine
engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)


# Create session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


# Database dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
