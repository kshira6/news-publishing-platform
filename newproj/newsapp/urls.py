from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Public view to list published articles
    path('', views.published_articles, name='published_articles'),

    # Admin views for managing articles
    path('manage/articles/', views.admin_article_list, name='admin_article_list'),
    path('manage/articles/create/', views.article_create, name='article_create'),
    path('manage/articles/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('manage/articles/<int:pk>/delete/', views.article_delete, name='article_delete'),

    # Authentication views
    path('login/', auth_views.LoginView.as_view(template_name='newsapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]