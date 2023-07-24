from sqlalchemy import Column, orm
from sqlalchemy.dialects.postgresql import (UUID, TEXT)
from .__database import Base
import uuid


class Role(Base):
    __tablename__ = "roles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(TEXT, nullable=False)
    permissions = Column(TEXT, nullable=False)  # Формат и виды прописаны в Readme

    users = orm.relationship("User", back_populates="role",
                             lazy="subquery")

    def __init__(self, title: str, permissions: str):
        """
        :param title: Название роли
        :param permissions: Полномочия конкретной роли
        """
        self.title = title
        self.permissions = permissions

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "permissions": self.permissions
        }