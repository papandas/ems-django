
from django.contrib import admin
from django.urls import path, include
from .views import index, details, vote

urlpatterns = [
    path('', index, name='polls_list'),
    path('<int:id>/details/', details, name='poll_details'),
    path('<int:id>/', vote, name='submit_vote')
]
