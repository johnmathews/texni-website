from django.shortcuts import render

# this is what django.views.generic.TemplateView does.
# this is an example, it is not needed.
def homeView(request):
    return render(request, "home.html", {})
