from django.urls import path
from django.views.generic import TemplateView

from donor import views

urlpatterns = [
    path('', views.DonorUser.as_view()),
    path('donor/', TemplateView.as_view(template_name="donor.html"))

]