from django.db import models

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    title = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = 'galleries'

    def __str__(self):
        return str(self.title)    