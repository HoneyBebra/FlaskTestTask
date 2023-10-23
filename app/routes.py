from flask import request, jsonify

from . import app
from app.services.questions import add_unique_question
from app.models import InteractionQuestion


@app.route('/', methods=['POST'])
def processing_query():
    data = request.json
    questions_num = data.get('questions_num')

    if questions_num is None or questions_num == 0 or not isinstance(questions_num, int):
        return jsonify(error='Invalid questions_num. Expected an integer > 0.'), 400

    interaction_question = InteractionQuestion()
    last_question = interaction_question.get_last_row()
    add_unique_question(questions_num, interaction_question)
    try:
        return last_question.question_text
    except AttributeError:
        return ''
