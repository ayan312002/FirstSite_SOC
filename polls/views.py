from django.core.serializers import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.db import IntegrityError
from .models import Question, Employee
from django.core import serializers
import json


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# Adds dummy data to database
def add_dummy(request):
    json_file = 'polls/templates/polls/employee.json'
    with open(json_file, 'r') as read_file:
        parsed_json = json.load(read_file)
    try:
        for result in parsed_json['data']:
            Employee.objects.update_or_create(
                id=result['id'],
                employee_name=result['employee_name'],
                profile_image=result['profile_image'],
                employee_age=result['employee_age'],
                employee_salary=result['employee_salary'],
            )
    except IntegrityError as e:
        raise Http404("Had some issues updating table.Try again after deleting it")

    return HttpResponse("You have added entries.")


def json_res(request):
    # json_file = 'polls/templates/polls/employee.json'
    # with open(json_file, 'r') as read_file:
    # parsed_json = json.load(read_file)
    # return JsonResponse(parsed_json)
    # response_data = [{'status': 'success'}]
    # for employee in Employee.objects.all():
    #    response_data.append([{'id': employee.id, 'employee_name': employee.employee_name}])  # this will make a list

    # print(response_data)
    # There are different methods.I liked this one since its simple

    queryset = Employee.objects.all()
    data = list(queryset.values())  # converts the queryset to a list

    qs_json = (serializers.serialize('json', queryset))

    # return JsonResponse(response_data, safe=False)
    return JsonResponse(data, safe=False)
    # return HttpResponse(qs_json)
