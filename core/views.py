from django.db.models import Avg
from django.core.exceptions import PermissionDenied
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
  fields = ['salon_name', 'zipcode', 'description', 'image_file']
  success_url = reverse_lazy('salon_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(SalonCreateView, self).form_valid(form)

from django.views.generic import ListView

class SalonListView(ListView):
  model = Salon
  template_name = "salon/salon_list.html"
  paginate_by = 5

from django.views.generic import DetailView

class SalonDetailView(DetailView):
  model = Salon
  template_name = 'salon/salon_detail.html'

  def get_context_data(self, **kwargs):
    context = super(SalonDetailView, self).get_context_data(**kwargs)
    salon = Salon.objects.get(id=self.kwargs['pk'])
    reviews = Review.objects.filter(salon=salon)
    context['reviews'] = reviews
    user_reviews = Review.objects.filter(salon=salon, user=self.request.user)
    context['user_reviews'] = user_reviews
    rating = Review.objects.filter(salon=salon).aggregate(Avg('rating'))
    context['rating'] = rating
    return context

from django.views.generic import UpdateView

class SalonUpdateView(UpdateView):
  model = Salon
  template_name = 'salon/salon_form.html'
  fields = ['salon_name', 'zipcode', 'description', 'image_file']

  def get_objects(self, *args, **kwargs):
    object = super(SalonUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

from django.views.generic import DeleteView

class SalonDeleteView(DeleteView):
  model = Salon
  template_name = 'salon/salon_confirm_delete.html'
  success_url = reverse_lazy('salon_list')

  def get_object(self, *args, **kwargs):
    object = super(SalonDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class ReviewCreateView(CreateView):
  model = Review
  template_name = "review/review_form.html"
  fields = ['text', 'visibility', 'rating']

  def get_success_url(self):
    return self.object.salon.get_absolute_url()

  def form_valid(self, form):
    salon = Salon.objects.get(id=self.kwargs['pk'])
    if Review.objects.filter(salon=salon, user=self.request.user).exists():
      raise PermissionDenied()
    form.instance.user = self.request.user
    form.instance.salon = Salon.objects.get(id=self.kwargs['pk'])
    return super(ReviewCreateView, self).form_valid(form)

class ReviewUpdateView(UpdateView):
  model = Review
  pk_url_kwarg = 'review_pk'
  template_name = 'review/review_form.html'
  fields = ['text','visibility','rating']

  def get_success_url(self):
    return self.object.salon.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(ReviewUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class ReviewDeleteView(DeleteView):
  model = Review
  pk_url_kwarg = 'review_pk'
  template_name = 'review/review_confirm_delete.html'

  def get_success_url(self):
    return self.object.salon.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(ReviewDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied
    return object

class UserDetailView(DetailView):
  model = User
  slug_field = 'username'
  template_name = 'user/user_detail.html'
  context_object_name = 'user_in_view'

  def get_context_data(self, **kwargs):
    context = super(UserDetailView, self).get_context_data(**kwargs)
    user_in_view = User.objects.get(username=self.kwargs['slug'])
    salons = Salon.objects.filter(user=user_in_view)
    context['salons'] = salons
    reviews = Review.objects.filter(user=user_in_view).exclude(visibility=1)
    context['reviews'] = reviews
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

class UserDeleteView(DeleteView):
  model = User
  slug_field = "username"
  template_name = 'user/user_confirm_delete.html'

  def get_success_url(self):
    return reverse_lazy('logout')

  def get_object(self, *args, **kwargs):
    object = super(UserDeleteView, self).get_object(*args, **kwargs)
    if object != self.request.user:
      raise PermissionDenied()
    return object

  def delete(self, request, *args, **kwargs):
    user = super(UserDeleteView, self).get_object(*args)
    user.is_active = False
    user.save()
    return redirect(self.get_success_url())

class SearchSalonListView(SalonListView):
  def get_queryset(self):
    incoming_query_string = self.request.GET.get('query','')
    return Salon.objects.filter(title_icontains=incoming_query_string)