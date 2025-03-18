from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('doc-register/',doc_register,name='doc_register'),
    path('doc-dashboard/',doc_dashboard,name='doc_dashboard'),
    path('doc-appointments/',appointments,name='appointments'),
    path('forget-password/',forget_password,name='forget_password'),
    path('search/',search,name='search'),

]

