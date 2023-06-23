from django.urls import path
from .import views
urlpatterns = [
    path('',views.Index.as_view(),name="indexes"),
    path('alert',views.get_alert,name='alert')
]
