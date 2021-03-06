from django.urls import path
from .views import home,data,search,signin,signup,logout_user


urlpatterns = [
    path('',home,name='home'),
    path('data_list/',data,name='data'),
    path('search/',search,name='search'),
    # Note auth
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('logout/',logout_user,name='logout'),
]