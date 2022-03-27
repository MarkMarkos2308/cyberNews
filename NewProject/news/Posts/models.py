from django.db import models

from django.db import models


class PostModel(models.Model):
    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images', null=True, blank=True)
    image3 = models.ImageField(upload_to='images', null=True, blank=True)
    image4 = models.ImageField(upload_to='images', null=True, blank=True)
    image5 = models.ImageField(upload_to='images', null=True, blank=True)
    image6 = models.ImageField(upload_to='images', null=True, blank=True)
    image7 = models.ImageField(upload_to='images', null=True, blank=True)
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=1500)
    type1 = models.IntegerField()

    def __str__(self):
        return f'id = {self.id} | {self.Title} | {self.type1}'
