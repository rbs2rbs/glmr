from django.shortcuts import render
from academico.scholar import *

import json

from random import randint
from django.views.generic import TemplateView
# Create your views here.

def academico (request):
    if request.method == 'GET':
        busca = {
            'busca' : request.GET.get('busca'),
            'tipo' : request.GET.get('tipo'),
            'token' : request.GET.get('token'),
            'titulos' : [],
            'p_chave' : {
                'valor' : [],
                'label' : [],
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

        return render(request,'academico.html', busca)
