from django.conf.urls import url
from pagina import views

urlpatterns = [
    url(r'^$',views.inicial),
    url(r'^email/$',views.email),
]