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
    offers       : so.WriteOnlyMapped['Offer']   = so.relationship(back_populates='user')

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


    user         : so.Mapped[User]             = so.relationship(back_populates='requests')
    offers       : so.WriteOnlyMapped['Offer'] = so.relationship(back_populates='request')


    def __repr__(self):
        return '<Request {}: "{}">'.format(self.title, self.description)
    
class Offer(db.Model):
    # Offers Table:
    # id (Primary Key)
    # request_id (Foreign Key from Requests)
    # user_id (Foreign Key from Users)
    # details
    # created_at (indexed)
    # updated_at

    id           : so.Mapped[int]           = so.mapped_column(primary_key=True)
    request_id   : so.Mapped[int]           = so.mapped_column(sa.ForeignKey(Request.id), index=True)
    user_id      : so.Mapped[int]           = so.mapped_column(sa.ForeignKey(User.id), index=True)

    description  : so.Mapped[str]           = so.mapped_column(sa.String(256))
    status       : so.Mapped[str]           = so.mapped_column(sa.Enum('Pending', 'Accepted', 'Rejected', 'Withdrawn'), nullable=False, default='Pending')

    created_at   : so.Mapped[datetime]      = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    updated_at   : so.Mapped[datetime]      = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))

    user         : so.Mapped[User]    = so.relationship(back_populates='offers')
    request      : so.Mapped[Request] = so.relationship(back_populates='offers')


    def __repr__(self):
        return '<Request {}: "{}">'.format(self.title, self.description)