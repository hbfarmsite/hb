from django.shortcuts import redirect, render
import re
from django.utils.timezone import datetime
from granja.forms import LogMessageForm
from granja.models import LogMessage
from django.views.generic import ListView


def index(request):
    return render(request, "granja/index.html")


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("index")
    else:
        return render(request, "granja/log_message.html", {"form": form})


class HomeListView(ListView):
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
