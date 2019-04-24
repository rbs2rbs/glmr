from django.conf.urls import url
from academico import views

urlpatterns = [
    # url('',views.academico, name = "academico"),
    url(r'^gettoken/$',views.gettoken, name = "gettoken"),
    url(r'^token/$',views.token, name = "token"),
    url(r'^token/busca',views.academico, name = "busca"),
]