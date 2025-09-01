from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('report/', views.report_animal, name='report_animal'),
    path('donate/', views.donate, name='donate'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('animal/<int:animal_id>/', views.animal_details, name='animal_details'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),  # Logout URL
    path('signup/', views.signup, name='signup'),  # If you have a signup view
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
