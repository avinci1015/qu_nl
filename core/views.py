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
from django.shortcuts import redirect
from django.views.generic import FormView
from .forms import *

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
        bar = bar.objects.get(id=self.kwargs['pk'])
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

class VoteFormView(FormView):
    form_class = VoteForm

    def form_valid(self, form):
        user = self.request.user
        bar = Bar.objects.get(pk=form.data["bar"])
        try:
            response = Response.objects.get(pk=form.data["response"])
            prev_votes = Vote.objects.filter(user=user, response=response)
            has_voted = (prev_votes.count()>0)
            if not has_voted:
                Vote.objects.create(user=user, response=response)
            else:
                prev_votes[0].delete()
            return redirect(reverse('bar_detail', args=[form.data["bar"]]))
        except:
            prev_votes = Vote.objects.filter(user=user, bar=bar)
            has_voted = (prev_votes.count()>0)
            if not has_voted:
                Vote.objects.create(user=user, bar=bar)
            else:
                prev_votes[0].delete()
        return redirect('bar_list')

class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    template_name = 'user/user_detail.html'
    context_object_name = 'user_in_view'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user_in_view = User.objects.get(username=self.kwargs['slug'])
        bars = Bar.objects.filter(user=user_in_view)
        context['bars'] = bars
        responses = Response.objects.filter(user=user_in_view)
        context['response'] = responses
        return context
      
class UserUpdateView(UpdateView):
    model = User
    slug_field = "username"
    template_name = "user/user_form.html"
    fields = ['email', 'first_name', 'last_name']
    
    def get_success_url(self):
        return reverse('user_detail', args=[self.request.user.username])

    def get_object(self, *args, **kwargs):
        object = super(UserUpdateView, self).get_object(*args, **kwargs)
        if object != self.request.user:
            raise PermissionDenied()
        return object      