from django.shortcuts import render, redirect
from lists.models import Item, List


def home_page(request):
    return render(request, "home.html")


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{list_.id}/")


def add_item(request, id=1):
    list_ = List.objects.get(id=id)
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{list_.id}/")


def view_list(request, id=1):
    list_ = List.objects.get(id=id)
    return render(request, "list.html", {"list": list_})
