from django.urls import path
from .import views


urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='top'),
    path('about/', views.about, name='about'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/add/', views.CreateNewsView.as_view(), name='news-add'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
]