from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request):
    html = "<html>"
    html += "<title>To-Do lists</title>"
    html += "</html>"
    return HttpResponse(html)
