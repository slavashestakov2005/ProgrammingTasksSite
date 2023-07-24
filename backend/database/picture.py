from sqlalchemy import Column, orm, ForeignKey
from sqlalchemy.dialects.postgresql import (UUID, TEXT, INTEGER)
from .__database import Base
import uuid


class Picture(Base):
    __tablename__ = "pictures"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"))
    path = Column(TEXT, nullable=False)
    order = Column(INTEGER, nullable=False)

    course = orm.relationship("Course")

    def __init__(self, course_id: uuid.UUID, path: str, order: int):
        """
        :param course_id: ID курса
        :param path: Путь до картинки
        :param order: Порядок картинок (число >= 0)
        """
        self.course_id = course_id
        self.path = path
        self.order = order

    def to_json(self):
        return {
            "id": self.id,
            "path": self.path,
            "order": self.order
        }