from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pagina.models import Postagem, Linkedin
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
import json

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
    form = ContactForm()
    return render(request,"index.html", {'postagem' : complete_posts, 'form' : form })


def email(request):
    if request.method == "POST" :
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        form = ContactForm(body)
        print(body)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            nome = form.cleaned_data['nome']
            message = "%s\n%s\n%s" % (nome, from_email,form.cleaned_data['message'])
            try:
                send_mail(subject, message, from_email,['renan.bisposilva@gmail.com','santana.guilherme@outlook.com'], fail_silently=True,)
            except BadHeaderError:
                return HttpResponse(
            json.dumps("Falha"),
            content_type= 'application/json',
            status= 500
        )
            return HttpResponse(
            json.dumps("OK"),
            content_type= 'application/json',
            status= 200
        )
        return HttpResponse(
            json.dumps("Erro interno no servidor"),
            content_type= 'application/json',
            status= 500
        )
