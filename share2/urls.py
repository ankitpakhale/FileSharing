from django.urls import path
from . import views

from django.conf.urls.static import static

urlpatterns = [
            # path('signup/',views.SignupView,name='SIGNUP2'),
            # path('login/',views.userLogin,name='LOGIN2'),
            path('logout/',views.userLogOut,name='LOGOUT2'),   
            path('dash/', views.dashboard, name='DASHBOARD2'),



            #-------------#
            path('login/', views.Login,name='login'),
            path('', views.index,name='index'),
            path('upload/', views.upload,name='upload'),
            
            path('signup/', views.SignUp,name='Signup'),
            
            path('loading/',views.loading,name='loading'),
            path('contact/', views.contact, name='contact'), 
            path('about/',views.about,name='about')
                    
          
]