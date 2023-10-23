import datetime
import requests
from pydantic import BaseModel


class DataCategory(BaseModel):
    id: int
    title: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    clues_count: int


class DataQuestion(BaseModel):
    id: int
    answer: str
    question: str
    value: int
    airdate: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    category_id: int
    game_id: int
    invalid_count: None
    category: DataCategory


class Question:
    def __init__(self):
        self.url = 'https://jservice.io/api/random?count='

    def parse_questions(self, questions_num: int):
        response = requests.get(self.url + str(questions_num))
        models = []
        for question in response.json():
            models.append(DataQuestion(**question))
        return models


def add_unique_question(questions_num: int, interaction_question):
    question = Question()
    while True:
        execute_count = 0
        models = question.parse_questions(questions_num)
        for model in models:
            execute_check = interaction_question.read(
                question_id=model.id, game_id=model.game_id, category_title=model.category.title,
                question_text=model.question, answer_text=model.answer, question_created_at=model.created_at
            )
            if execute_check:
                execute_count += 1
                continue
            interaction_question.create(
                question_id=model.id, game_id=model.game_id, category_title=model.category.title,
                question_text=model.question, answer_text=model.answer, question_created_at=model.created_at
            )
        if execute_count > 0:
            questions_num = execute_count
        else:
            break
