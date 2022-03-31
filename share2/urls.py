from django.urls import path
from . import views

from django.conf.urls.static import static

urlpatterns = [
            path('signup/',views.SignupView,name='SIGNUP2'),
            path('login/',views.userLogin,name='LOGIN2'),
            path('logout/',views.userLogOut,name='LOGOUT2'),   
            path('dash/', views.dashboard, name='DASHBOARD2'),
            
          
]