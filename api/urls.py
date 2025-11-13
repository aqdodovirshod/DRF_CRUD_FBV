from django.urls import path
from .views import post_list_create_api_view, post_detail_update_delete_api_view
from .views import BookListView


urlpatterns = [
    path("posts/", post_list_create_api_view),
    path("posts/<int:pk>/", post_detail_update_delete_api_view),
    path('books/', BookListView.as_view(), name='book-list'),
]