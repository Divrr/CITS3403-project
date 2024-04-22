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

    requests     : so.WriteOnlyMapped['Request'] = so.relationship(back_populates='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Request(db.Model):
    # Requests Table schema:
    # id (Primary Key)
    # user_id (Foreign Key from Users)
    # title
    # description
    # status
    # created_at (indexed)
    # updated_at

    id           : so.Mapped[int]           = so.mapped_column(primary_key=True)
    user_id      : so.Mapped[int]           = so.mapped_column(sa.ForeignKey(User.id), index=True)

    title        : so.Mapped[str]           = so.mapped_column(sa.String(64))
    description  : so.Mapped[str]           = so.mapped_column(sa.String(256))
    status       : so.Mapped[str]           = sa.Column(sa.Enum('Open', 'Closed', 'Pending', 'Completed'), nullable=False, default='Open')

    created_at   : so.Mapped[datetime]      = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    updated_at   : so.Mapped[datetime]      = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))


    user         : so.Mapped[User] = so.relationship(back_populates='requests')


    def __repr__(self):
        return '<Request {}: "{}">'.format(self.title, self.description)