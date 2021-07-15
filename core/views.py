from django.views.generic import FormView
from .models import Servico, Funcionario, Recurso, Cliente
from django.urls import reverse_lazy
from django.contrib import messages

from django.utils.translation import gettext as _
from django.utils import translation

from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        _lang_ = translation.get_language()  # seleciona o idioma atraves do navegador
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = list(Recurso.objects.order_by('?').all())
        context['lang'] = _lang_
        context['clientes'] = list(Cliente.objects.order_by('?').all())

        translation.activate(_lang_)

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso.'))
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro no envio do E-mail'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
