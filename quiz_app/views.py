import random

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Answer, Quiz


def get_answers(question_id):
    answers = Answer.objects.filter(question_id=question_id)
    return answers


def index(request):
    return render(request, 'quiz_app/index.html', {})


def quiz_init(request):
    quizzes = Quiz.objects.all()
    quiz = random.choice(quizzes)
    request.session['quiz_id'] = quiz.id
    request.session['number_of_questions'] = len(quiz.questions.all())
    request.session['question_number'] = 0
    request.session['number_true_answers'] = 0
    return redirect('quiz_app:quiz_start')


def quiz_start(request):
    question_number = request.session.get('question_number', 0)
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        current_question_id = request.POST.get('current_question_id')
        true_answer = Answer.objects.filter(question_id=current_question_id).get(true_answer=True)
        if int(user_answer) == int(str(true_answer)):
            request.session['number_true_answers'] += 1
        request.session['question_number'] += 1
        return HttpResponseRedirect(reverse('quiz_app:quiz_start'))
    else:
        if question_number < request.session.get('number_of_questions'):
            quiz = Quiz.objects.get(pk=request.session['quiz_id'])
            current_question = quiz.questions.all()[question_number]
            answers = Answer.objects.filter(question_id=current_question.id)
            context = {'current_question': current_question, 'answers': answers}
            return render(request, 'quiz_app/quiz_start.html', context)
        else:
            return HttpResponseRedirect(reverse('quiz_app:quiz_finish'))


def quiz_finish(request):
    number_of_true_answers = int(request.session.get('number_true_answers'))
    number_of_questions = int(request.session.get('number_of_questions'))
    user_rate = round((number_of_true_answers/number_of_questions) * 100, 1)
    context = {
        'user_rate': user_rate,
        'number_of_true_answers': number_of_true_answers,
        'number_of_questions': number_of_questions
    }
    return render(request, 'quiz_app/quiz_finish.html', context)
