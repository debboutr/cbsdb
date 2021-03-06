from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('waiver/', views.waiver, name='waiver'),
    path('addbike/', views.addbike, name='addbike'),
    path('bikelist/', views.BikeListView.as_view(), name='bikelist'),
    path('bikelist/<int:pk>', views.BikeDetailView.as_view(), name='bike-detail'),
]
