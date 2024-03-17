from django.urls import path
from informations.views.information import (toutInformation, detailInformation,
                                            creerInformation, suprimerInformation,
                                            InformationUpdateView)

urlpatterns = [
    path('information/get-all-information/', toutInformation, name='toutInformation'),
    path('information/detail-information/<int:pk>/', detailInformation, name='detailinformation'),
    path('information/creer-Information/', creerInformation, name='creerInformation'),
    path(' information/delete-information/', suprimerInformation, name='suprimerInformation'),
    path('information/information-updateView/<int:pk>/', InformationUpdateView.as_view(), name='InformationUpdateView'),
    
] 