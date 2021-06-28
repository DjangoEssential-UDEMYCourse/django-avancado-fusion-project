from django.contrib import admin
from .models import Cargo, \
                    Servico, \
                    Funcionario, \
                    Recurso, \
                    Cliente, \
                    Comentario \


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'criacao', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'criacao', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao', 'ativo', 'modificado')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('comentario', 'cliente')
