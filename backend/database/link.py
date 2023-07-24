from sqlalchemy import Column, orm, ForeignKey
from sqlalchemy.dialects.postgresql import (UUID, TEXT)
from .__database import Base
import uuid


class Link(Base):
    __tablename__ = "useful_links"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey("lessons.id"))
    title = Column(TEXT)
    link = Column(TEXT)

    lesson = orm.relationship("Lesson")

    def __init__(self, title: str, link: str, lesson_id: uuid.UUID):
        """
        :param title: название ссылки
        :param link: ссылка на ресурс
        :param lesson_id: UUID урока, к которому привязана ссылка
        """
        self.link = link
        self.lesson_id = lesson_id
        self.title = title

    def to_json(self) -> dict:
        return {
            "link": self.link,
            "title": self.title,
        }