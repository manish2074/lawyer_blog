from django.db import models
from django.urls import reverse
# Create your models here.
class Legal(models.Model):
    title = models.CharField(max_length=150)
    created_date = models.DateField(auto_now=True)
    story = models.TextField()
    slug = models.SlugField(max_length=255,null=True,blank=True,default="mansih")

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = 'legals'    
        
    def get_absolute_url(self):
        return reverse('legal_detail',kwargs={"slug":self.slug,"pk":self.pk})

class Events(models.Model):
    title = models.CharField(max_length=150)
    created_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='events')
    story = models.TextField()
    slug = models.SlugField(max_length=255,null=True,blank=True,default="mansih")
    def __str__(self):
        return str(self.title)   

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = 'events'    

    def get_absolute_url(self):
        return reverse('event_detail',kwargs={"slug":self.slug,"pk":self.pk})
    