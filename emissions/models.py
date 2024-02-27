from django.db import models

# Create your models here.

class Emissions(models.Model):
    nom = models.CharField(max_length = 128)
    image = models.FileField(upload_to='assets/imagesemissions/',
                             default='',blank=True, max_length=250)
    video = models.FileField(upload_to='assets/videoemissions/',
                             default='',blank=True, max_length=250)
    audio =models.FileField(upload_to='assets/audioemissions/',
                             default='',blank=True, max_length=250)
    
    def __str__(self) :
        return self.nom