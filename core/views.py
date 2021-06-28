from django.views.generic import TemplateView
from .models import Servico, Funcionario, Recurso, Cliente


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = list(Recurso.objects.order_by('?').all())
        context['clientes'] = list(Cliente.objects.order_by('?').all())

        return context
