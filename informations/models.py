from django.db import models

from account.models import CustomUser

# Create your models here.

class Information(models.Model):

    titre = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='assets/imagesinformation/',
                             default='',blank=True, max_length=250)
    user  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                               related_name='userinformation', null=True, blank=True)
    
    def __str__(self):
        return self.titre
    