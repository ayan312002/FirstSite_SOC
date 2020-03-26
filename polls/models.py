import datetime

from django.db import models
from django.utils import timezone


def get_image_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.id(), filename)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_salary = models.PositiveIntegerField(default=0)
    employee_age = models.PositiveIntegerField(default=0)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.employee_name

    def id(self):
        self.id()
