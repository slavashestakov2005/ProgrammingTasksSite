from sqlalchemy import Column, orm, ForeignKey
from sqlalchemy.dialects.postgresql import (UUID, TEXT, INTEGER)
from .__database import Base
import uuid


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"))
    name = Column(TEXT)
    description = Column(TEXT)
    order = Column(INTEGER, nullable=False, default=0)

    course = orm.relationship("Course")
    links = orm.relationship("Link",
                             back_populates="lesson",
                             cascade="all, delete",
                             lazy="subquery")
    tasks = orm.relationship("Task",
                             back_populates="lesson",
                             cascade="all, delete",
                             lazy="subquery")

    def __init__(self, name: str, description: str, course_id: uuid.UUID, order: int):
        """
        :param name: Название урока
        :param description: Описание урока
        :param course_id: UUID курса, к которому привязан урок
        :param order: Порядок уроков в курсе
        """
        self.name = name
        self.description = description
        self.course_id = course_id
        self.order = order

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "tasks": [task.to_json() for task in self.tasks],
            "links": [link.to_json() for link in self.links],
            "order": self.order
        }