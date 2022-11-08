from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "index.html"

class OnedayschedulelistView(generic.TemplateView):
    template_name = "onedayschedulelist.html"

class OneweekschedulelistView(generic.TemplateView):
    template_name = "oneweekschedulelist.html"