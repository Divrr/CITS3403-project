from datetime import datetime, timezone
from sqlalchemy import String, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, WriteOnlyMapped, mapped_column, relationship
from typing import Optional
from app import db

class User(db.Model):
    id           : Mapped[int]           = mapped_column(primary_key=True)
    username     : Mapped[str]           = mapped_column(String(64), nullable=False, index=True, unique=True)
    email        : Mapped[str]           = mapped_column(String(128), nullable=False, index=True, unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(256))

    authored     : WriteOnlyMapped['Activity'] = relationship(back_populates='author', foreign_keys='Activity.author_id')
    accepted     : WriteOnlyMapped['Activity'] = relationship(back_populates='acceptor', foreign_keys='Activity.acceptor_id')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Activity(db.Model):
    id           : Mapped[int]      = mapped_column(primary_key=True)
    author_id    : Mapped[int]      = mapped_column(ForeignKey(User.id), nullable=False)
    acceptor_id  : Mapped[int]      = mapped_column(ForeignKey(User.id), nullable=True)

    type         : Mapped[str]      = mapped_column(Enum('Request', 'Offer'))
    category     : Mapped[str]      = mapped_column(String(15), nullable=False)
    description  : Mapped[str]      = mapped_column(String(100), nullable=False)

    status       : Mapped[str]      = mapped_column(Enum('Open', 'Pending', 'Closed'), nullable=False, default='Open')
    updated_at   : Mapped[datetime] = mapped_column(index=True, nullable=False, default=lambda: datetime.now(timezone.utc))

    author       : Mapped[User] = relationship(back_populates='authored', foreign_keys=[author_id])
    acceptor     : Mapped[User] = relationship(back_populates='accepted', foreign_keys=[acceptor_id])


    def __repr__(self):
        return '<Request {}: "{}">'.format(self.category, self.description)