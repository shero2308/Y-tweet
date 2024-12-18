from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    path('',views.tweet_list,name='tweet_list'),

    path('create/',views.tweet_create,name='create_tweet'),

    path('<int:tweet_id>/edit/',views.tweet_edit,name='edit_tweet'),

    path('<int:tweet_id>/delete/',views.tweet_delete,name='delete_tweet'),

    path('register/',views.register,name='register'),

    ]
