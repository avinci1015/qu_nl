from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class BarCreateView(CreateView):
    model = Bar
    template_name = "bar/bar_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('Bar_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BarCreateView, self).form_valid(form)

class BarListView(ListView):
    model = Bar
    template_name = "bar/bar_list.html"

class BarDetailView(DetailView):
    model = Bar
    template_name = 'bar/bar_detail.html'

class BarUpdateView(UpdateView):
    model = Bar
    template_name = 'bar/bar_form.html'
    fields = ['title', 'description']
    
class BarDeleteView(DeleteView):
    model = Bar
    template_name = 'bar/bar_confirm_delete.html'
    success_url = reverse_lazy('bar_list')    