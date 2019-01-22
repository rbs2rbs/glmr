from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pagina.models import Postagem, Linkedin
from django.utils import timezone
from django.contrib.auth.models import User

def inicial(request):
    postagem = Postagem.objects.filter(data_publicado__lte=timezone.now()).order_by('data_publicado') [:3]
    complete_posts = []
    for post in postagem:
        linkedin = Linkedin.objects.filter(usuario=post.autor).first().linkedin
        imagem_autor =  Linkedin.objects.filter(usuario=post.autor).first().imagem_usuario
        complete_posts.append({
            'post': post,
            'linkedin': linkedin,
            'imagem_autor': imagem_autor
        })
    return render(request,"index.html", {'postagem' : complete_posts })
