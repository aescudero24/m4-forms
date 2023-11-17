from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import AddForm

# Create your views here.


def root_view(request: HttpRequest) -> HttpResponse:
    print(request.GET)
    return render(request, "root.html")


def add_view(request):
    form = AddForm(request.GET)
    if form.is_valid():
        x = form.cleaned_data["x"]
        y = form.cleaned_data["y"]
        answer = x + y
        return render(
            request, "add.html", {"form": form, "x": x, "y": y, "answer": answer}
        )
    else:
        return render(request, "add.html", {"form": form})
