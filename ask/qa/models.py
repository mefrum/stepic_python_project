# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField(default=1)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='to_owner_q')
    likes = models.ManyToManyField(User)


class Answer(models.Model):
    text = models.TextField(null=False)
    added_at = models.DateField()
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)


class QuestionManager(models.Model):
    def new(self):
       return Question.objects.order_by('added_at')[0:10]

    def popular(self):
        return Question.objects.order_by('rating')[0:10]