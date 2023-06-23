from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('homepage',views.HomePage.as_view(),name="homepage"),
    path('registration',views.Registration.as_view(),name='register'),
    path('update',views.UpdateProfile.as_view(),name='update-profile'),
    path('logins',views.MyLogin.as_view(),name='login'),
    path('logout',views.MyLogout.as_view(),name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/<uidb64>/<token>/',views.MyPasswordResetConfirmView,name ='password_reset_confirm' ),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
   
]
