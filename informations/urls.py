from django.urls import path
from informations.views.information import (toutInformation, detailInformation,
                                            creerInformation, suprimerInformation,
                                            InformationUpdateView)

urlpatterns = [
    path('information/getallinformation/', toutInformation, name='toutInformation'),
    path('information/detailinformation/<int:pk>/', detailInformation, name='detailinformation'),
    path('information/creerInformation/', creerInformation, name='creerInformation'),
    path(' ', suprimerInformation, name='suprimerInformation'),
    path('information/InformationUpdateView/<int:pk>/', InformationUpdateView.as_view(), name='InformationUpdateView'),
    
] 