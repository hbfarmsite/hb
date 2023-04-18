from django.urls import path
from granja import views
from granja.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="granja/index.html",
)

urlpatterns = [
    path("", home_list_view, name="index"),
    path("log/", views.log_message, name="log"),
]
