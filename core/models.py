import os
import uuid

def upload_to_location(instance, filename):
  blocks = filename.split('.')
  ext = blocks[-1]
  filename = "%s.%s" % (uuid.uuid4(), ext)
  instance.title = blocks[0]
  return os.path.join('uploads/', filename)

from django.core.urlresolvers import reverse
RATING_CHOICES = (
(0, 'None'),
(1, '*'),
(2, '**'),
(3, '***'),
(4, '****'),
(5, '*****'),
)
VISIBILITY_CHOICES = (
(0, 'Public'),
(1, 'Anonymous'),
)
from django.db import models

from django.contrib.auth.models import User

class Salon(models.Model):
  salon_name = models.CharField(max_length=300)
  zipcode = models.CharField(max_length=10)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)
  image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)


  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("salon_detail", args=[self.id])

class Review(models.Model):
  salon = models.ForeignKey(Salon)
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add=True)
  text = models.TextField()
  visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)
  rating = models.IntegerField(choices=RATING_CHOICES, default=0)

  def __unicode__(self):
    return self.text
