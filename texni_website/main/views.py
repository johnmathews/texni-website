from django.shortcuts import render
from django.views.generic.edit import FormView
from main import forms



def home(request):
    context = {
        'background': 'jshine.jpg',
    }
    return render(request, 'home.html', context)


def about_us(request):
    context = {
        'background': 'amin.jpg',
    }
    return render(request, 'about_us.html', context)


#  def contact(request):
#      context = {
#          'background': 'jshine.jpg',
#      }
#      return render(request, 'contact_form.html', context)


def team(request):
    context = {
        'background': 'harvey.jpg',
    }
    return render(request, 'team.html', context)


def case_studies(request):
    context = {
        'background': 'cool-sky.jpg',
    }
    return render(request, 'case_studies.html', context)


def careers(request):
    context = {
        'background': 'magetron.jpg',
    }
    return render(request, 'careers.html', context)


def events(request):
    context = {
        'background': 'witching-hour.jpg',
    }
    return render(request, 'events.html', context)


class ContactUsView(FormView):
    template_name = "contact_form.html" # this is how it knows which template to use in urls.py
    form_class = forms.ContactForm # this is how it knows which form to use in the template
    success_url = "/"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['background'] ='jshine.jpg'
        return context


    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
