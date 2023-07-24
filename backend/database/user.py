from sqlalchemy import Column, orm, ForeignKey
from sqlalchemy.dialects.postgresql import (UUID, TEXT)
from werkzeug.security import generate_password_hash, check_password_hash
from .__database import Base
import uuid
from .course import Course


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(TEXT, nullable=False)
    login = Column(TEXT, nullable=False, unique=True)
    email = Column(TEXT, nullable=False)
    password = Column(TEXT, nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))

    role = orm.relationship("Role")
    courses = orm.relationship("Course", secondary="users_to_courses",
                               backref="courses",
                               lazy="subquery")
    solves = orm.relationship("Solve",
                              back_populates="user",
                              cascade="all, delete")
    authors_courses = orm.relationship("Course", back_populates="author",
                                       lazy="subquery")

    def __init__(self, name: str, login: str, email: str, role_id: uuid.UUID):
        """
        :param name: Имя пользователя
        :param login: Логин пользователя
        :param email: Почта пользователя
        :param role_id: ID роли
        """
        self.name = name
        self.login = login
        self.email = email
        self.role_id = role_id

    def generate_hash_password(self, password: str):
        self.password = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password, password)

    def check_perm(self, *permissions) -> bool:
        """
        Метод для проверки полномочий
        :param permissions:
        :type permissions: Tuple[str]
        :return: True, если у пользователя есть переданные полномочия
        """
        return all([i in self.role.permissions or f"/{i[1:].capitalize()}" in self.role.permissions
                    for i in permissions])

    def check_course(self, course: Course) -> bool:
        """
        Метод проверяет нахождение пользователя на курсе
        :param course: курс, нахождение на котором мы проверяем
        """
        for user_course in self.courses:
            if course.id == user_course.id:
                return True
        return False

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "login": self.login,
            "email": self.email,
            "role": self.role.to_json(),
            "courses": [course.to_json() for course in self.courses]
        }

    def get_solves(self) -> dict:
        return {"solves": [solve.to_json() for solve in self.solves]}
