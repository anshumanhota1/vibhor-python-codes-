from django.urls import path
from . import views


urlpatterns = [
   path('', views.post_view, name='home'),
   path('create/', views.post_create),
   path('<str:slug>/', views.post_details, name='detail'),
   path('<str:slug>/edit/', views.post_update, name='update'),
   path('<str:slug>/delete/', views.post_delete, name='delete'),
]