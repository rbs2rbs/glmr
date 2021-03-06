from django.shortcuts import render
from academico.scholar import *
from urllib.parse import urlparse
from django.http import HttpResponse


import json

from random import randint
from django.views.generic import TemplateView
# Create your views here.

def gettoken(request):
    if request.method == "GET":
        return render(request,'gettoken.html')


def token(request):
    
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        request.session['token'] = body
        return HttpResponse(
            json.dumps("OK"),
            content_type= 'application/json',
            status= 200
        )
    return render(request,'token.html')




def academico (request):
    if request.method == 'GET':
        busca = {
            'busca' : request.GET.get('busca'),
            'tipo' : request.GET.get('tipo'),
            'token' : request.session['token'],
            'titulos' : [],
            'p_chave' : {
                'valor' : [],
                'label' : [],
                },
            'anos': {
                'valor' : [],
                'ano' : []
                }
            }
        
        if (busca['busca']!="" and busca['busca']!= None and busca['tipo']!="" and busca['tipo']!= None):
            dados = Scholar(
                busca = busca['busca'], 
                tipo = busca['tipo'], 
                token = busca['token']
            )
        
            dados.gerar()
            
            p_chaves = grafico('palavras-chave',dados)
            
            for index,p_chave in enumerate(p_chaves):
                busca['p_chave']['valor'].append(p_chave[1])
                busca['p_chave']['label'].append(p_chave[0])

                if (index == 9): break
            
            busca['p_chave']['label'] = json.dumps(busca['p_chave']['label'])
            busca['p_chave']['valor'] = json.dumps(busca['p_chave']['valor'])
            
            for titulo in dados.saida:
                busca['titulos'].append(titulo['titulo'])


            for an,v in grafico('ano',dados).items():
                busca['anos']['valor'].append(int(v))
                busca['anos']['ano'].append(int(an))

        return render(request,'academico.html', busca)
    else:
        return render(request,'token.html')
    

