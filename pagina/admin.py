from django.contrib import admin
from pagina.models import Postagem, Linkedin

class Adicao(admin.ModelAdmin):
    class Media:
        css = {
            "screen": ("css/codeblok.css",),
        }

        # js = ("js/laxtexFuncoes.js",)



admin.site.register(Postagem,Adicao)
admin.site.register(Linkedin)
# Register your models here.
