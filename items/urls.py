from django.urls import path
from .views import PostItemListView, PostItemDetailView, PostItemCreateView


urlpatterns = [
    path('', PostItemListView.as_view(), name='home'),
    path('listings/<int:pk>/', PostItemDetailView.as_view(), name='list-detail'),
    path('listings/new/', PostItemCreateView.as_view(), name='new-listing'),

]
