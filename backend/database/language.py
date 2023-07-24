from sqlalchemy import Column, orm
from sqlalchemy.dialects.postgresql import (UUID, TEXT)
from .__database import Base
import uuid


class Language(Base):
    __tablename__ = "languages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(TEXT, nullable=False)
    path = Column(TEXT, nullable=False)
    options = Column(TEXT)

    courses = orm.relationship("Course",
                               back_populates="language",
                               cascade="all, delete",
                               lazy="subquery")

    def __init__(self,
                 name: str,
                 path: str,
                 options: str = ""):
        """
        :param name: Название языка программирования
        :param path: путь до сервера, на котором выполняется тестирование
        :param options: опции скрипта запуска
        """
        self.name = name
        self.path = path
        self.options = options

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name
        }