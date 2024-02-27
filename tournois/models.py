from django.db import models

from account.models import CustomUser


class Tournois(models.Model):
    nom  = models.CharField(max_length = 128)
    date = models.CharField(max_length = 128, blank = True)
    lieu = models.CharField(max_length = 128, blank = True)
    participant = models.IntegerField(default = 1)
    description = models.TextField(blank = True)
    image = models.FileField(upload_to='assets/imagestournoi/',
                             default='',blank=True, max_length=250)
    user  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                               related_name='usertournoi', null=True, blank=True)
    
    
    def __str__(self):
        return self.nom