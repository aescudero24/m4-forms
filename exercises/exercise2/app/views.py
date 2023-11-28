from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from app.forms import FrontTimesForm, NoTeenSumForm, XyzThereForm, CenteredAverageForm

# Create your views here.


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def front_times_view(request: HttpRequest) -> HttpResponse:
    form = FrontTimesForm(request.GET)
    if form.is_valid():
        string = form.cleaned_data["string"]
        number = form.cleaned_data["number"]
        result = string[: min(3, len(string))] * number
        return render(request, "front.html", {"form": form, "result": result})
    else:
        return render(request, "front.html", {"form": form})


def no_teen_sum_view(request: HttpRequest) -> HttpResponse:
    def check_teen(n):
        return n if n not in [13, 14, 17, 18, 19] else 0

    form = NoTeenSumForm(request.GET)
    if form.is_valid():
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        c = form.cleaned_data["c"]
        sum = check_teen(a) + check_teen(b) + check_teen(c)
        return render(request, "noteen.html", {"form": form, "sum": sum})
    else:
        return render(request, "noteen.html", {"form": form})


def xyz_there_view(request: HttpRequest) -> HttpResponse:
    form = XyzThereForm(request.GET)
    if form.is_valid():
        string = form.cleaned_data["string"]
        for i in range(len(string) - 2):
            if string[i : i + 3] == "xyz" and (i == 0 or string[i - 1] != "."):
                verdict = True
                break
            else:
                verdict = False
        return render(request, "xyz.html", {"form": form, "verdict": verdict})
    else:
        return render(request, "xyz.html", {"form": form})


def centered_average_view(request: HttpRequest) -> HttpResponse:
    def centered_average(numbers):
        return (sum(numbers) - min(numbers) - max(numbers)) / (len(numbers) - 2)

    form = CenteredAverageForm(request.GET)
    if form.is_valid():
        numbers = form.cleaned_data["numbers"]
        result = format(centered_average(numbers), ".0f")
        return render(request, "centeravg.html", {"form": form, "result": result})
    else:
        return render(request, "centeravg.html", {"form": form})
