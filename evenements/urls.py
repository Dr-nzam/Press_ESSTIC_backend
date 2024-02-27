from django.urls import path
from .views.events import (allEvenement, detailEvenement,EvenementUpdateView,
                           ajouterEvent, suprimerEvent)

urlpatterns = [
    path('evenement/all-event/', allEvenement, name= 'all-event'),
    path('evenement/detail-event/<int:pk>/', detailEvenement, name= 'detail-event'),
    path('evenement/update-event/<int:pk>/', EvenementUpdateView.as_view(), name= "update-event"),
    path('evenement/ajouter-event/', ajouterEvent, name= 'ajouter-event'),
    path('evenement/suprimer-event/<int:pk>/', suprimerEvent, name= 'suprimer-event'),
]