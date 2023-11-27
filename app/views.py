from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import AddForm, SignUpForm

# Create your views here.


def root_view(request: HttpRequest) -> HttpResponse:
    context = {}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            context["signup_success"] = True
    else:
        form = SignUpForm()
    context["form"] = form
    return render(request, "root.html", context)


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
