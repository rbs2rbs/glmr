from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Linkedin(models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    linkedin = models.URLField(default='', blank=True)
    imagem_usuario = models.ImageField(upload_to="avatar_usuario/",  blank=True, null=True)    


    def __str__(self):
        return "%s" %(self.usuario)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        

class Postagem(models.Model):
    autor = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default = timezone.now)
    data_publicado = models.DateTimeField(blank = True, null = True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo




# Create your models here.
