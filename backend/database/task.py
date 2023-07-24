from sqlalchemy import Column, orm, ForeignKey
from sqlalchemy.dialects.postgresql import (UUID, TEXT, JSON, BIGINT, INTEGER)
from .__database import Base
import uuid


class Task(Base):
    __tablename__ = "tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey("lessons.id"))
    name = Column(TEXT)
    task_condition = Column(TEXT)
    tests = Column(JSON)
    time_limit = Column(BIGINT)
    order = Column(INTEGER)
    type_id = Column(UUID(as_uuid=True), ForeignKey("task_types.id"))

    task_type = orm.relationship("TaskType")
    lesson = orm.relationship("Lesson")
    solves = orm.relationship("Solve",
                              back_populates="task",
                              cascade="all, delete",
                              lazy="subquery")

    def __init__(self, name: str,
                 task_condition: str,
                 tests: dict,
                 lesson_id: uuid.UUID,
                 order: int,
                 time_limit: int = 1):
        """
        :param name: Название задания
        :param task_condition: Условие задания
        :param tests: JSON с тестами
        :param order: Порядок отображения задач
        :param lesson_id: UUID урока, к которому привязано задание
        :param time_limit: Лимит времени на выполнение кода
        """
        self.name = name
        self.task_condition = task_condition
        self.tests = tests
        self.lesson_id = lesson_id
        self.time_limit = time_limit
        self.order = order

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "task_condition": self.task_condition,
            "time_limit": self.time_limit,
            "tests": self.tests["tests"][:2],
            "order": self.order
        }
