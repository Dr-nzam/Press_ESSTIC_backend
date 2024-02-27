from django.urls import path
from .views.tournoi import (allTournois, detailTournoi,TournoiUpdateView, 
                            ajouterTournoi, suprimerTounoi)

urlpatterns = [
    path('tournois/tout-tournoi/', allTournois, name = 'tout-tournoi'),
    path('tournois/detail-tournoi/<int:pk>/', detailTournoi, name = 'detail-tournoi'),
    path('tournois/update-tournoi/<int:pk>/', TournoiUpdateView.as_view(), name = 'update-tournoi'),
    path('tournois/ajouter-tournoi/', ajouterTournoi, name = 'ajouter-tournoi'),
    path('tournois/suprimer-tournoi/<int:pk>/', suprimerTounoi, name = 'suprimer-tournoi'),
]
