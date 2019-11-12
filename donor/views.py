from django.views.generic import FormView
from donor.forms import DonorForm
from donor.models import Donor


class DonorUser(FormView):
    template_name = "login.html"
    form_class = DonorForm
    success_url = '/donor/'

    def form_valid(self, form):
        if form.is_valid():
            user_name = form.cleaned_data.get("user_name")
            password = form.cleaned_data.get("password")
            res = Donor.objects.get(user_name=user_name,password=password)
            if res:
                return super().form_valid(form)
            else:
                return
        else:
            return self.form_invalid()