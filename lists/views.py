from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from lists.models import Item


# Create your views here.


def home_page(request: HttpRequest) -> HttpResponse:
    """Домашняя страница"""
    if request.method == "POST":
        Item.objects.create(text=request.POST["item_text"])
        return redirect("/lists/the-only-list-in-the-world")

    items = Item.objects.all()
    return render(request, "home.html", {"items": items})


def view_list(request: HttpRequest) -> HttpResponse:
    """представление списка"""
    items = Item.objects.all()
    return render(request, "home.html", {"items": items})
