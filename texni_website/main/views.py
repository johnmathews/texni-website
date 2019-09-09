from django.shortcuts import render
from django.views.generic.edit import FormView
from main import forms

# this is what django.views.generic.TemplateView does.
# this is an example, it is not needed.
def homeView(request):
    return render(request, "home.html", {})


class ContactUsView(FormView):
    template_name = "contact_form.html" # this is how it knows which template to use in urls.py
    form_class = forms.ContactForm # this is how it knows which form to use in the template
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)

def home(request):
    context = {
        'background': 'jshine.jpg',
        'view-name': 'home',
    }
    return render(request, 'home.html', context)
