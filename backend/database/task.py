from .__db_session import sa, SqlAlchemyBase, Table


class Task(SqlAlchemyBase, Table):
    __tablename__ = 'task'
    fields = ['id', 'title', 'content_text', 'input_text', 'output_text']

    id = sa.Column(sa.Integer, nullable=False, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    content_text = sa.Column(sa.String, nullable=False)
    input_text = sa.Column(sa.String, nullable=False)
    output_text = sa.Column(sa.String, nullable=False)
