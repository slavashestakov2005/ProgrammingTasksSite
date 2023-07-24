from sqlalchemy import Column, orm, ForeignKey
from sqlalchemy.dialects.postgresql import (UUID, TEXT, DATE, BIGINT)
from .__database import Base
import datetime
import uuid


class Solve(Base):
    __tablename__ = "solves"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    verdict = Column(TEXT)
    code = Column(TEXT)
    time = Column(BIGINT)
    date = Column(DATE, default=datetime.datetime.now)

    task = orm.relationship("Task")
    user = orm.relationship("User")

    def __init__(self, task_id: uuid.UUID,
                 user_id: uuid.UUID,
                 code: str,
                 time: int = 0,
                 verdict: str = "Check"):
        """
        :param task_id: UUID задания
        :param user_id: UUID пользователя
        :param code: код, отправленный на проверку
        :param time: время выполнения кода
        :param verdict: результат выполнения кода
        """
        self.task_id = task_id
        self.user_id = user_id
        self.code = code
        self.verdict = verdict
        self.time = time

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "task": self.task.to_json(),
            "verdict": self.verdict,
            "code": self.code,
            "time": self.time,
            "date": self.date
        }