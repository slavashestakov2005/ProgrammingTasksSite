from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import (UUID, DATE)
from .__database import Base
import datetime
import uuid


class Attendance(Base):
    __tablename__ = "users_to_courses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    date = Column(DATE, default=datetime.datetime.now)

    def __init__(self, course_id: uuid.UUID, user_id: uuid.UUID):
        """
        :param course_id: UUID курса, к которому прикрепляется пользователь
        :param user_id: UUID пользователя
        """
        self.course_id = course_id
        self.user_id = user_id