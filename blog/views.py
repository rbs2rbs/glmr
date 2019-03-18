from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from pagina.models import Postagem, Linkedin
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def blog(request):
    postagem = Postagem.objects.filter(data_publicado__lte=timezone.now()).order_by('data_publicado') 
    complete_posts = []
    for post in postagem:
        linkedin = Linkedin.objects.filter(usuario=post.autor).first().linkedin
        imagem_autor =  Linkedin.objects.filter(usuario=post.autor).first().imagem_usuario
        complete_posts.append({
            'post': post,
            'linkedin': linkedin,
            'imagem_autor': imagem_autor
        })
    
    paginacao = Paginator(complete_posts,1)

    pagina = request.GET.get('pagina')

    complete_posts = paginacao.get_page(pagina)

    return render(request,"blog.html", 
        {
            'postagem' : complete_posts, 
            'postagem_titulo': postagem ,
            'pagina':int(pagina), 
            'proxima_pagina' : int(pagina)+1
        })
