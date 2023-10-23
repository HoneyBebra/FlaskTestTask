import datetime
from sqlalchemy import create_engine, desc
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import sessionmaker

import config


engine = create_engine(url=config.ENGINE_URL, echo=config.SQLALCHEMY_ECHO)


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[int]
    category_title: Mapped[str] = mapped_column(String(255))
    question_text: Mapped[str]
    answer_text: Mapped[str]
    question_created_at: Mapped[datetime.datetime]
    row_created_at: Mapped[datetime.datetime]


class InteractionQuestion:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def create(
            self, question_id: int, game_id: int, category_title: str, question_text: str, answer_text: str,
            question_created_at: datetime.datetime
    ):
        new_question = Question(
            id=question_id, game_id=game_id, category_title=category_title, question_text=question_text,
            answer_text=answer_text, question_created_at=question_created_at, row_created_at=datetime.datetime.now()
        )
        session = self.Session()
        session.add(new_question)
        session.commit()
        session.close()

    def read(
            self, question_id=None, game_id=None, category_title=None, question_text=None, answer_text=None,
            question_created_at=None, row_created_at=None
    ):
        session = self.Session()
        questions = session.query(Question)
        if question_id is not None:
            questions = questions.filter(Question.id == question_id)
        if game_id is not None:
            questions = questions.filter(Question.game_id == game_id)
        if category_title is not None:
            questions = questions.filter(Question.category_title == category_title)
        if question_text is not None:
            questions = questions.filter(Question.question_text == question_text)
        if answer_text is not None:
            questions = questions.filter(Question.answer_text == answer_text)
        if question_created_at is not None:
            questions = questions.filter(Question.question_created_at == question_created_at)
        if row_created_at is not None:
            questions = questions.filter(Question.row_created_at == row_created_at)
        session.close()
        return questions.all()

    def update(self):
        pass

    def delete(self):
        pass

    def get_last_row(self):
        session = self.Session()
        last_row = session.query(Question).order_by(desc(Question.row_created_at)).first()
        session.close()
        return last_row


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
