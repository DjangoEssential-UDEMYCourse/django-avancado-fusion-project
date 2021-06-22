from django.views.generic import TemplateView


class IndexView(TemplateView):
	template_name = 'index.html'


class P404View(TemplateView):
	template_name = '404.html'
