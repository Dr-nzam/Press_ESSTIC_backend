from django.urls import path
from .views.emission import (allEmission, detailEmission, EmissionUpdateView,
                             ajouterEmission, suprimerEmission)


urlpatterns = [
    path('emission/tout-emission/', allEmission, name="tout-emission"),
    path('emission/detail-emission/<int:pk>/', detailEmission, name="detail-emission"),
    path('emission/update-emission/<int:pk>/', EmissionUpdateView.as_view(), name="update-emission"),
    path('emission/ajouter-emission/', ajouterEmission, name='ajouter-emission'),
    path('emission/suprimer-emission/<int:pk>/', suprimerEmission, name="suprimer-emission"),
]
