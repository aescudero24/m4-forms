from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from app.forms import HeyForm, AgeForm, OrderForm


# Create your views here.
def hey_view(request: HttpRequest) -> HttpResponse:
    form = HeyForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        return render(request, "hey.html", {"form": form, "name": name.title()})
    else:
        return render(request, "hey.html", {"form": form})


def age_view(request: HttpRequest) -> HttpResponse:
    form = AgeForm(request.GET)
    if form.is_valid():
        end = form.cleaned_data["end"]
        birthyear = form.cleaned_data["birthyear"]
        answer = abs(end - birthyear)
        return render(request, "age.html", {"form": form, "answer": answer})
    else:
        return render(request, "age.html", {"form": form})


def order_view(request: HttpRequest) -> HttpResponse:
    form = OrderForm(request.GET)
    if form.is_valid():
        burgers = form.cleaned_data["burgers"]
        fries = form.cleaned_data["fries"]
        drinks = form.cleaned_data["drinks"]
        total = format(burgers * 4.50 + fries * 1.50 + drinks, ".2f")
        return render(request, "order.html", {"form": form, "total": total})
    else:
        return render(request, "order.html", {"form": form})
