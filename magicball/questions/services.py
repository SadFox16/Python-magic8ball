import random

from .models import *


def get_question_count(question):
    question_cnt = History.objects.filter(question=question).count()
    return question_cnt


def get_random_answer():
   ids = Answers.objects.all().order_by('?').values_list('pk', flat=True)
   pk = random.randint(0, len(ids)-1)
   rand = Answers.objects.get(pk=ids[pk])
   return rand


def get_last_answer(question, user, answer_id):
    answer = History.objects.filter(question=question, user=user).order_by('-created_date').first()
    if answer and answer.id == answer_id:
        return get_last_answer(question, user, get_random_answer().id)
    return answer


def get_answer(user, question):
    answer = get_random_answer()
    history = History(
        user=user,
        answer=get_random_answer(),
        question=question,
    )
    history.save()
    data = {
        'answer': history.answer.answer,
        'question_cnt': get_question_count(history.question)
    }
    return data