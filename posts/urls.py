from django.urls import path
from . import views


urlpatterns = [
   path('', views.post_view),
   path('create/', views.post_create),
   path('<int:id>/', views.post_details),
   path('update/', views.post_update),
   path('delete/', views.post_delete),
]