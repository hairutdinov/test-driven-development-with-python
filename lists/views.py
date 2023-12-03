from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from lists.models import Item
from lists.models import List


# Create your views here.


def home_page(request: HttpRequest) -> HttpResponse:
    """Домашняя страница"""
    return render(request, "home.html")


def view_list(request: HttpRequest, list_id) -> HttpResponse:
    """представление списка"""
    list_ = List.objects.get(id=list_id)
    return render(request, "list.html", {"list": list_})


def new_list(request: HttpRequest) -> HttpResponse:
    mylist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=mylist)
    return redirect(f"/lists/{mylist.id}")


def add_item(request: HttpRequest, list_id) -> HttpResponse:
    list_ = List.objects.get(pk=list_id)
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{list_.id}")
