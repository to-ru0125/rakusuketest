from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index2.html"
