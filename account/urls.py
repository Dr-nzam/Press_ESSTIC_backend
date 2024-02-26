from django.urls import path
from .views import ChangePasswordAPI,registerUser, logout  
from .views import CustomTokenObtainPairView
   

urlpatterns = [
    path('account/create-user/', registerUser, name='register-user'),
    path('account/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('account/logout/', logout, name='logout'),
    path('change-password/', ChangePasswordAPI.as_view(), name='change-password'),
    
]