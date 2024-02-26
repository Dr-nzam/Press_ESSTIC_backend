from django.db import models

# Create your models here.

class Information(models.Model):

    titre = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(upload_to='assets/imagesinformation/',
                             default='',blank=True, max_length=250)
    
    def __str__(self):
        return self.titre
    