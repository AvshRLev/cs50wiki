from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("wiki/", views.entry, name= "wiki"),
    path("wiki/<str:entry>", views.entry, name="wiki_entry"),
    path("new/", views.new, name="new"),
    path("edit/", views.edit, name="edit"),
    path("edit_save/", views.edit_save, name="edit_save"),
    path("random/", views.random, name="random")
]
