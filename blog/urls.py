from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home_view, name='home'),  
    path('short/', views.time_pass, name='short'),  
    path('p/<slug:slug>/', views.post_detail_view, name='post-detail'),  
    path('twit/new/', views.twit_create_view, name='twit-create'), 
    path('twit/<slug:slug>/', views.twit_detail_view, name='twit-detail'), 
    path('image/new/', views.post_create_view, name='post-create'),
    path('video/new/', views.video_create_view, name='video-create'),
    path('post/<int:pk>/update/', views.post_update_view, name='post-update'),  
    path('post/<int:pk>/delete/', views.post_delete_view, name='post-delete'), 
    path('search/users/', views.search_view, name='search'), 
    path('like/post', views.like_view, name='like'),
    path('report/post/', views.post_report_view, name='report'),
    path('report/user/', views.user_report_view, name='report-user'),
    path('<str:username>/notifications/', views.notifications_view, name='notifications'),
    path('<str:username>/notifications/update/', views.notifications_update_view, name='notifications-update'),
    path('<str:username>/notifications/count/', views.notifications_unread_count_view, name='notifications-count'),
]
