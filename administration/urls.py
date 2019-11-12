from django.urls import path
from django.views.generic import TemplateView, CreateView

from administration import views

urlpatterns = [
    path('', views.Admin.as_view()),
    path('welcome_admin/', TemplateView.as_view(template_name="welcome_admin.html")),
    path('addorganization/', views.AddOrganizations.as_view(), name="addorganization"),

]