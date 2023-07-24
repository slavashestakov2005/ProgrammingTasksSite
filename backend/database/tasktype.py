from sqlalchemy import Column, orm
from sqlalchemy.dialects.postgresql import (UUID, TEXT)
from .__database import Base
import uuid


class TaskType(Base):
    __tablename__ = "task_types"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(TEXT, nullable=False)
    format = Column(TEXT, nullable=False)

    tasks = orm.relationship("Task", back_populates="task_type",
                             lazy="subquery")

    def __init__(self, title: str, _format: str):
        """
        :param title: Название типа
        :param _format: формат (смотри в Readme)
        """
        self.title = title
        self.format = _format

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "format": self.format
        }