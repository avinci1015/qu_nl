from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.core.exceptions import PermissionDenied

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class BarCreateView(CreateView):
    model = Bar
    template_name = "bar/bar_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('bar_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BarCreateView, self).form_valid(form)

class BarListView(ListView):
    model = Bar
    template_name = "bar/bar_list.html"

class BarDetailView(DetailView):
    model = Bar
    template_name = 'bar/bar_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BarDetailView, self).get_context_data(**kwargs)
        bar = Bar.objects.get(id=self.kwargs['pk'])
        responses = Response.objects.filter(bar=bar)
        context['responses'] = responses
        return context

class BarUpdateView(UpdateView):
    model = Bar
    template_name = 'bar/bar_form.html'
    fields = ['title', 'description']

    def get_object(self, *args, **kwargs):
        object = super(BarUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class BarDeleteView(DeleteView):
    model = Bar
    template_name = 'bar/bar_confirm_delete.html'
    success_url = reverse_lazy('bar_list')

    def get_context_data(self, **kwargs):
        context = super(BarDetailView, self).get_context_data(**kwargs)
        bar = Bar.objects.get(id=self.kwargs['pk'])
        response = Response.objects.filter(bar=bar)
        context['response'] = response
        user_response = Response.objects.filter(bar=bar, user=self.request.user)
        context['user_respond'] = user_respond
        return context

    def get_object(self, *args, **kwargs):
        object = super(BarDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object


class ResponseCreateView(CreateView):
    model = Response
    template_name = "response/response_form.html"
    fields = ['text']

    def get_success_url(self):
        return self.object.bar.get_absolute_url()


    def form_valid(self, form):
        bar = Bar.objects.get(id=self.kwargs['pk'])
        if Response.objects.filter(bar=bar, user=self.request.user).exists():
            raise PermissionDenied()
        form.instance.user = self.request.user
        form.instance.bar = Bar.objects.get(id=self.kwargs['pk'])
        return super(ResponseCreateView, self).form_valid(form)



class ResponseUpdateView(UpdateView):
    model = Response
    pk_url_kwarg = 'response_pk'
    template_name = 'response/response_form.html'
    fields = ['text']

    def get_success_url(self):
        return self.object.bar.get_absolute_url()

    def get_object(self, *args, **kwargs):
        object = super(ResponseUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class ResponseDeleteView(DeleteView):
    model = Response
    pk_url_kwarg = 'response_pk'
    template_name = 'response/response_confirm_delete.html'

    def get_success_url(self):
        return self.object.bar.get_absolute_url()

    def get_object(self, *args, **kwargs):
        object = super(ResponseDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object