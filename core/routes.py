from django.urls import path
from .views import IndexView, P404View

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('404', P404View.as_view(), name='404'),
]
