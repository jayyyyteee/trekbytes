from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="post-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail"), #/posts/my-first-post
    path("aboutme", views.AboutMeView.as_view(), name="about-me"),
    path("trackme/", views.TrackLocationView.as_view(), name="track-me")
]