from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

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
    data_criacao = models.DateTimeField(default = timezone.now)
    data_publicado = models.DateTimeField(blank = True, null = True)
    texto = MarkdownxField()
    resumo = MarkdownxField()

    @property
    def formatted_markdown_texto(self):
        return markdownify(self.texto)

    def formatted_markdown_resumo(self):
        return markdownify(self.resumo)      

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo




# Create your models here.
