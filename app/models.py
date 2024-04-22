from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    # Users Table schema:
    # id (Primary Key)
    # username
    # email
    # password_hash
    # created_at
    # updated_at

    id           : so.Mapped[int]           = so.mapped_column(primary_key=True)

    username     : so.Mapped[str]           = so.mapped_column(sa.String(64), index=True, unique=True)
    email        : so.Mapped[str]           = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    created_at   : so.Mapped[datetime]      = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    updated_at   : so.Mapped[datetime]      = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return '<User {}>'.format(self.username)