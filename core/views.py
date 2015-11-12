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
  success_url = reverse_lazy('salon_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(SalonCreateView, self).form_valid(form)

from django.views.generic import ListView

class SalonListView(ListView):
  model = Salon
  template_name = "salon/salon_list.html"

from django.views.generic import DetailView

class SalonDetailView(DetailView):
  model = Salon
  template_name = 'salon/salon_detail.html'

  def get_context_data(self, **kwargs):
    context = super(SalonDetailView, self).get_context_data(**kwargs)
    salon = Salon.objects.get(id=self.kwargs['pk'])
    review = Review.objects.filter(salon=salon)
    context['review'] = review
    return context

from django.views.generic import UpdateView

class SalonUpdateView(UpdateView):
  model = Salon
  template_name = 'salon/salon_form.html'
  fields = ['salon_name', 'description']

from django.views.generic import DeleteView

class SalonDeleteView(DeleteView):
  model = Salon
  template_name = 'salon/salon_confirm_delete.html'
  success_url = reverse_lazy('question_list')

class ReviewCreateView(CreateView):
  model = Review
  template_name = "review/review_form.html"
  fields = ['text']

  def get_success_url(self):
    return self.object.salon.get_absolute_url()

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.salon = Salon.objects.get(id=self.kwargs['pk'])
    return super(ReviewCreateView, self).form_valid(form)

class ReviewUpdateView(UpdateView):
  model = Review
  pk_url_kwarg = 'review_pk'
  template_name = 'review/review_form.html'
  fields = ['text']

  def get_success_url(self):
    return self.objects.question.get_absolute_url()

class ReviewDeleteView(DeleteView):
  model = Review
  pk_url_kwarg = 'review_pk'
  template_name = 'review/review_confirm_delete.html'

  def get_success_url(self):
    return self.object.salon.get_absolute_url()