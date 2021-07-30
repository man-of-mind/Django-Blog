from timmyBlog.views import HomePage
from django.urls import path
from .views import DetailPost, HomePage, AddPostView, UpdatePostView, DeletePostView, AddCommentView, LikeView, DislikeView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('detailsPost/<int:pk>', DetailPost.as_view(), name="detail-post"),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('dislike/<int:pk>', DislikeView, name="dislike_post"),
    path('add_new_post/', AddPostView.as_view(), name="add-post"),
    path('articles/edit/<int:pk>', UpdatePostView.as_view(), name="edit-post"),
    path('articles/delete/<int:pk>', DeletePostView.as_view(), name="delete-post"),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name="add-comment"),
]