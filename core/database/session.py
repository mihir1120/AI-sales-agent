from sqlalchemy import create_engine

from core.config.settings import get_settings


engine = create_engine(get_settings().database_url, pool_pre_ping=True)
