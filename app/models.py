from datetime import datetime, timezone
from sqlalchemy import String, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, WriteOnlyMapped, mapped_column, relationship
from typing import Optional
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app import login

class User(UserMixin, db.Model):
    id           : Mapped[int]           = mapped_column(primary_key=True)
    username     : Mapped[str]           = mapped_column(String(64), nullable=False, index=True, unique=True)
    email        : Mapped[str]           = mapped_column(String(128), nullable=False, index=True, unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(256))

    authored     : WriteOnlyMapped['Activity'] = relationship(back_populates='author', foreign_keys='Activity.author_id')
    accepted     : WriteOnlyMapped['Activity'] = relationship(back_populates='acceptor', foreign_keys='Activity.acceptor_id')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def accept(self, activity):
        if not self.has_accepted(activity):
            activity.status = 'Pending'
            activity.acceptor_id = self.id
            db.session.add(activity)
            
    def resolve(self, activity):
        if self.has_authored(activity):
            activity.status = 'Closed'
            db.session.add(activity)
    
    def cancel(self, activity):
        if self.has_accepted(activity):
            activity.status = 'Open'
            activity.acceptor_id = None
            self.accepted.remove(activity)
            db.session.add(activity)
            db.session.add(self)

    def has_accepted(self, activity):
        query = self.accepted.select().where(Activity.id == activity.id)
        return db.session.scalar(query) is not None
    
    def has_authored(self, activity):
        query = self.authored.select().where(Activity.id == activity.id)
        return db.session.scalar(query) is not None

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

    author       : Mapped[User] = relationship(back_populates='authored', foreign_keys=[author_id])
    acceptor     : Mapped[User] = relationship(back_populates='accepted', foreign_keys=[acceptor_id])

    def __repr__(self):
        return '<Request {}: "{}">'.format(self.category, self.description)

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))