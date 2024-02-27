from django.db import models

class Evenement (models.Model):
    nom = models.CharField(max_length = 250)
    date = models.CharField(max_length=128, blank=True)
    heureDebut = models.CharField(max_length = 128,  blank = True)
    heureFin = models.CharField(max_length = 128,  blank = True)
    lieu = models.CharField(max_length = 128, blank = True)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='assets/imagesevenement/',
                             default='',blank=True, max_length=250)
    
    def __str__(self) :
        return self.nom