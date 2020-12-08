from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("wiki", views.entry, name= "wiki"),
    path("new/", views.new, name="new"),
    path("edit/", views.edit, name="edit"),
    path("edit_save/", views.edit, name="edit_save")
]
