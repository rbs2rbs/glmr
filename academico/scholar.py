# PARA FAZER O PARSE HTML
from bs4 import BeautifulSoup as BS
# PARA FAZER AS REQUISIÇÕES HTTP
import requests
# UTILIZAR REGEX PARA ESTRAIR TEXTOS
import re

import matplotlib.pyplot as plt

# Create random data with numpy
import numpy as np
import pandas as pd

import collections

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 


class Scholar(object):
  def __init__(self,busca,tipo,token):
    self.url_inicial = "https://api.mendeley.com/search/catalog?%s=%s&limit=100" %(tipo,"%22"+busca.replace(" ","%20")+"%22")
    self.headers = {
          'Authorization': 'Bearer '+token,
          'Accept' : 'application/vnd.mendeley-document.1+json'
          }
    self.req = requests.get(self.url_inicial, headers = self.headers, timeout = 5)
    self.saida = []
    self.qt_artigos = None
    self.titulos = None
    self.anos = None

  def gerar(self):
    print(self.req.status_code)
    if self.req.status_code != 200:
      print('Token Expirado\nhttps://mendeley-show-me-access-tokens.herokuapp.com/')
      return('Token Expirado')
    else:
      for dados in self.req.json():
        if "keywords" in dados.keys():
          self.saida.append(
            {
              'titulo' : dados['title'],
              'ano' : dados['year'],
              'resumo' : dados['abstract'],
              'palavras' : dados['keywords']
            }
          )
        else :
          self.saida.append(
            {
              'titulo' : dados['title'],
              'ano' : dados['year'],
              'resumo' : dados['abstract']
            }
          )

      proximo = self.req.links
      if proximo:
        while proximo:
          url = proximo['next']['url'] 
          req = requests.get(url, headers = self.headers, timeout = 5)
          print(req.status_code)
          for dados in req.json():
            if "keywords" in dados.keys():
              self.saida.append(
                {
                  'titulo' : dados['title'],
                  'ano' : dados['year'],
                  'resumo' : dados['abstract'],
                  'palavras' : dados['keywords']
                }
              )
            else :
              self.saida.append(
                {
                  'titulo' : dados['title'],
                  'ano' : dados['year'],
                  'resumo' : dados['abstract']
                }
              )
                
          proximo = req.links    

    self.qt_artigos = len(self.saida)/2
   

def grafico(t,dados):
  if not t in ["ano","titulo","resumo","palavras-chave"]:
      return ("Tipo de grafico Inválido")
  if t == "ano":
    # ANALISE ANO

    anos = []
    for ano in dados.saida:
        anos.append(ano['ano'])

    anos_np = np.unique(anos, return_counts=True)
    for index, i in enumerate(range(min(anos_np[0]),max(anos_np[0])+1)):
        if i not in anos:
            anos_np = np.insert(anos_np,[index],[[i],[0]], axis=1)

    plt.plot(anos_np[0], anos_np[1], 'r--')
    plt.show()

  elif t == "titulo":
    # ANALISE TITULO

    stop_words_in = set(stopwords.words('english')) 
    stop_words_pt = set(stopwords.words('portuguese')) 

    titulo_filtrado = [] 
    for titulo in dados.saida:
        word_tokens = word_tokenize(titulo['titulo']) 
        for w in word_tokens:
            if not (w.lower() in stop_words_in or w.lower() in stop_words_pt):
                if w.isalnum():
                    titulo_filtrado.append(w.lower())

    titulo_filtrado = collections.Counter(titulo_filtrado).most_common()

    df = pd.DataFrame(titulo_filtrado[:10])

    p = df.plot(kind='barh', title ="Palavras Frequentes", figsize=(15, 10), legend=False, fontsize=12)
    p.set_yticklabels(df[0])
    p.invert_yaxis()
    plt.show()

  elif t == "resumo":

    # ANALISE RESUMO

    stop_words_in = set(stopwords.words('english')) 
    stop_words_pt = set(stopwords.words('portuguese')) 

    resumo_filtrado = [] 
    for resumo in dados.saida:
        word_tokens = word_tokenize(titulo['resumo']) 
        for w in word_tokens:
            if not (w.lower() in stop_words_in or w.lower() in stop_words_pt):
                if w.isalnum():
                    resumo_filtrado.append(w.lower())

    resumo_filtrado = collections.Counter(resumo_filtrado).most_common()

    df = pd.DataFrame(resumo_filtrado[:10])

    p = df.plot(kind='barh', title ="Palavras Frequentes", figsize=(15, 10), legend=False, fontsize=12)
    p.set_yticklabels(df[0])
    p.invert_yaxis()
    plt.show()
  
  elif t == "palavras-chave":

    palavra_filtrado = []

    for palavra in dados.saida:
      if "palavras" in palavra.keys():
        for p in palavra['palavras']:
          palavra_filtrado.append(p.lower())

    palavra_filtrado = collections.Counter(palavra_filtrado).most_common()

    return (palavra_filtrado)

    df = pd.DataFrame(palavra_filtrado[:10])

    p = df.plot(kind='barh', title ="Palavras Frequentes", figsize=(15, 10), legend=False, fontsize=12)
    p.set_yticklabels(df[0])
    p.invert_yaxis()
    plt.show()
