from django.urls import path
from . import views
from rest.views import ApiListView, ApiDeleteView

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('post-detail/<str:pk>/', views.postDetail, name="postDetail"),
    path('post-create/', views.postCreate, name="postCreate"),
    path('post-update/<str:pk>', views.postUpdate, name="postUpdate"),
    path('post-delete/<str:pk>', ApiDeleteView.as_view(), name="postDelete"),
    path('post-list', ApiListView.as_view(), name='list'),
]