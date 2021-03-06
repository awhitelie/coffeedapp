from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='location_list', args=[self.id])
