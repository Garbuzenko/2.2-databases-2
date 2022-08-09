from django.db.models import Count
from django.views.generic import ListView
from django.shortcuts import render
# import query_debugger
from .models import Student, Teacher


# @query_debugger
from .utils import query_debugger


@query_debugger
def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.prefetch_related
    # students = Student.objects.all()
    context = {'students': students}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = 'group'

    return render(request, template, context)
