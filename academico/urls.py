from django.conf.urls import url
from academico import views

urlpatterns = [
    url('',views.academico, name = "academico")
]