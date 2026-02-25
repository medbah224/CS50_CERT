from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mohamed", views.mohamed, name="mohamed"),
    path("<str:name>", views.great, name="great")
]