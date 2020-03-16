from django.urls import path
from . import views


urlpatterns = [
   path('', views.post_view),
   path('create/', views.post_create),
   path('<int:id>/', views.post_details, name='detail'),
   path('<int:id>/edit/', views.post_update, name='update'),
   path('delete/', views.post_delete),
]