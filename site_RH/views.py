import http
from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render


def my_view(request):
    return render(request, 'funcionarios/home.html')
