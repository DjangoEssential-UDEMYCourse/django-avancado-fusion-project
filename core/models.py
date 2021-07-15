import uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import  gettext_lazy as _


def get_file_path(_instance, _file_name):
    ext = _file_name.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criacao = models.DateField(_('Criação'), auto_now_add=True)
    modificado = models.DateField(_('Atualizado'), auto_now=True)
    ativo = models.BooleanField(_('Ativo?'), default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', _('Engrenagem')),
        ('lni-stats-up', _('Gráfico')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
    )

    servico = models.CharField(_('Serviço'), max_length=100)
    descricao = models.CharField(_('Descrição'), max_length=200)
    icone = models.CharField(_('Icone'), max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField(_('Cargo'), max_length=100)

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField(_('Equipe'), max_length=100)
    cargo = models.ForeignKey('core.cargo', verbose_name=_('Cargo'), on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField(_('Imagem'), upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    tweeter = models.CharField('Tweeter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')

    def __str__(self):
        return self.nome


class Recurso(Base):
    ICONE_CHOICES = (
        ('lni-leaf"', _('Pluma')),
        ('lni-laptop-phone', _('Multi-Plataforma')),
        ('lni-support', _('Suporte')),
        ('lni-lock', _('Segurança')),
        ('lni-bolt', _('Velocidade')),
        ('lni-coffee-cup', _('Cafe Em Paz')),
    )
    nome = models.CharField(_('Nome'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=200)
    icone = models.CharField(_('Icone'), max_length=50, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Recurso')
        verbose_name_plural = _('Recursos')

    def __str__(self):
        return self.nome


class Cliente(Base):
    nome = models.CharField(_('Nome'), max_length=100)
    profissao = models.CharField(_('Profissão'), max_length=100)
    imagem = StdImageField(_('Imagem'), upload_to=get_file_path, variations={'thumb': {'width': 75, 'height': 75, 'crop': True}}, default='')

    class Meta:
        verbose_name = _("Cliente")
        verbose_name_plural = _("Clientes")

    def __str__(self):
        return self.nome


class Comentario(Base):
    comentario = models.TextField('Comentário', max_length=500)
    cliente = models.OneToOneField(Cliente,
                                   verbose_name=_("Cliente"),
                                   on_delete=models.CASCADE,
                                   primary_key=True)

    class Meta:
        verbose_name = _("Comentario")
        verbose_name_plural = _("Comentarios")

    def __str__(self):
        return self.comentario
