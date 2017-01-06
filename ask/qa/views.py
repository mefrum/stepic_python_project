
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import Question, QuestionManager
from django.contrib.auth.models import User


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK',content_type='text/html', status = 200)


def home_page(request, *args, **kwargs):
    test = "test"
    template = "index.html"
    u = User(username=test, password=test, first_name="ftest", last_name="ltest")
    u.save()
    question_list = [
        {
            "name": "",
            "build_url": "123",
            "created_date": "date"
        },
    ]
    return render_to_response(template,{
        'question_list': question_list
    })

