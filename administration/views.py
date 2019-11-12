from django.views.generic.edit import FormView, CreateView
from administration.models import Administration, Organization
from administration.forms import AdminForm


class Admin(FormView):
    template_name = "administration.html"
    form_class = AdminForm
    success_url = '/administration/welcome_admin/'

    def form_valid(self, form):
        if form.is_valid():
            user_name = form.cleaned_data.get("user_name")
            password = form.cleaned_data.get("password")
            Administration(user_name=user_name, password=password).save()
            return super().form_valid(form)
        else:
            return self.form_invalid()


class AddOrganizations(CreateView):
    model = Organization
    template_name = "addorganization.html"
    fields = "__all__"
    success_url = "/administration/welcome_admin/"
