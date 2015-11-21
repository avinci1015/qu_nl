from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Bar(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("bar_detail", args=[self.id])

class Response(models.Model):
    bar = models.ForeignKey(Bar)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __unicode__(self):
        return self.text
      
class Vote(models.Model):
    user = models.ForeignKey(User)
    bar = models.ForeignKey(Bar, blank=True, null=True)
    response = models.ForeignKey(Response, blank=True, null=True)
    
    def __unicode__(self):
        return "%s upvoted" % (self.user.username)     