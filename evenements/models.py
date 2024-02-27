from django.db import models
from account.models import CustomUser

class Evenement (models.Model):
    nom = models.CharField(max_length = 250)
    date = models.CharField(max_length=128, blank=True)
    heureDebut = models.CharField(max_length = 128,  blank = True)
    heureFin = models.CharField(max_length = 128,  blank = True)
    lieu = models.CharField(max_length = 128, blank = True)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='assets/imagesevenement/',
                             default='',blank=True, max_length=250)
    user  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                               related_name='userevent', null=True, blank=True)
    
    def __str__(self) :
        return self.nom