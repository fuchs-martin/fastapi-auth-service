from logging.config import fileConfig

from sqlalchemy import create_engine, pool
from alembic import context

from app.database import Base
from app.config import settings

from app import models

# Alembic Config object
config = context.config

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for autogenerate
target_metadata = Base.metadata


def get_database_url() -> str:
    """
    Normalize DATABASE_URL for SQLAlchemy.
    Fly.io provides postgres://, SQLAlchemy expects postgresql+psycopg://
    """
    return settings.DATABASE_URL.replace(
        "postgres://",
        "postgresql+psycopg://",
        1,
    )


def run_migrations_offline() -> None:
    """Run migrations in offline mode."""
    url = get_database_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in online mode."""
    connectable = create_engine(
        get_database_url(),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
