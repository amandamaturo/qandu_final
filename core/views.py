from django.shortcuts import render

from django.views.generic import TemplateView

class Home(TemplateView):
  template_name = "home.html"

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import*

class SalonCreateView(CreateView):
  model = Salon
  template_name = "salon/salon_form.html"
  fields = ['salon_name', 'description']
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(SalonCreateView, self).form_valid(form)
