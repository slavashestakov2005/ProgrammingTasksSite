from sqlalchemy import Column, orm, ForeignKey
from sqlalchemy.dialects.postgresql import (UUID, TEXT, BOOLEAN)
from .__database import Base
import uuid


class Course(Base):
    __tablename__ = "courses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(TEXT, nullable=False)
    description = Column(TEXT, nullable=False)
    pic = Column(TEXT)  # Путь до картинки
    language_id = Column(UUID(as_uuid=True), ForeignKey("languages.id"))
    is_public = Column(BOOLEAN, default=True, nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    language = orm.relationship("Language")
    author = orm.relationship("User")
    lessons = orm.relationship("Lesson",
                               back_populates="course",
                               cascade="all, delete",
                               lazy="subquery")
    users = orm.relationship("User", secondary="users_to_courses",
                             backref="users",
                             lazy="subquery")
    pictures = orm.relationship("Picture", back_populates="course",
                                lazy="subquery")

    def __init__(self, name: str,
                 description: str,
                 language_id: uuid.UUID,
                 is_public=True):
        """
        :param name: Название курса
        :param description: Описание курса
        :param language_id: UUID языка программирования,
         на котором решается курс
        :param is_public: True если курс публичный
        """
        self.name = name
        self.description = description
        # self.pic = pic
        self.language_id = language_id
        self.is_public = is_public

    def __repr__(self):
        return f"<Course '{self.name}'>"

    def check_user(self, user):
        for user_at_course in self.users:
            if user.id == user_at_course.id:
                return True
        return False

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "pic": self.pic,
            "id": self.id,
            "language": self.language.to_json(),
            "is_public": self.is_public,
            "lessons": [lesson.to_json() for lesson in self.lessons]
        }