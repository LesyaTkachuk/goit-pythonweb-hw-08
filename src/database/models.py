from datetime import datetime, date
from typing import Optional

from sqlalchemy import Column, Integer, String, Boolean, Table, func
from sqlalchemy.orm import relationship, mapped_column, Mapped, DeclarativeBase
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import DateTime, Date


class Base(DeclarativeBase):
    pass


contact_m2m_group = Table(
    "contact_m2m_group",
    Base.metadata,
    Column(
        "contact_id",
        Integer,
        ForeignKey("contact.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    Column(
        "group_id",
        Integer,
        ForeignKey("group.id", ondelete="CASCADE", onupdate="CASCADE"),
    ),
    PrimaryKeyConstraint("contact_id", "group_id"),
)


class Contact(Base):
    __tablename__ = "contact"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    surname: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    birthday: Mapped[date] = mapped_column(DateTime, nullable=False)
    address_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("address.id"), nullable=True, default=None
    )
    is_active: Mapped[bool] = mapped_column("is_active",Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        "created_at", DateTime, default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        "updated_at", DateTime, default=func.now(), onupdate=func.now()
    )
    groups: Mapped[list["Group"]] = relationship(
        "Group", secondary=contact_m2m_group, back_populates="contacts"
    )


class Group(Base):
    __tablename__ = "group"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(50), nullable=False, unique=True)
    contacts: Mapped[list["Contact"]] = relationship(
        "Contact", secondary=contact_m2m_group, back_populates="groups"
    )


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    country: Mapped[str] = mapped_column(String(50), nullable=False)
    index: Mapped[int] = mapped_column(Integer, nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    street: Mapped[str] = mapped_column(String(50), nullable=False)
    house: Mapped[str] = mapped_column(String(4), nullable=False)
    apartment: Mapped[str] = mapped_column(String(4))
