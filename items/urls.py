from django.urls import path
from .views import PostItemListView, PostItemCreateView


urlpatterns = [
    path('', PostItemListView.as_view(), name='home'),
    path('listings/new/', PostItemCreateView.as_view(), name='new-listing'),

]
