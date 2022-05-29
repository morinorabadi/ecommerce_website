from django.urls import path, include

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', TemplateView.as_view(template_name='admin/index.html')),
    path('', TemplateView.as_view(template_name='index/index.html')),
    path('login/', TemplateView.as_view(template_name='login/index.html')),
]
