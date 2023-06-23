from django.urls import path
from . import views
urlpatterns = [
    path('',views.Styling.as_view(),name='radio'),
]
