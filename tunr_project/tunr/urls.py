from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist_detail'),
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('songs/<int:pk>/', views.SongDetail.as_view(), name='song_detail')

]

# The path takes three arguments:

# The first argument represents the URL path. Here, the artist list is going to be rendered in the root URL. Similar to the "/" URL in other languages, the path of the root URL starts, ends, and has nothing in between. In Django, we do not even need to include the /. This way of doing URLs is great because they are explicit. We no longer have to reorder or rename URLs in order to make them work!
# The URL's second argument is the view function this route is going to match up with in the view file. So, at the root URL, the application will run the artist_list function we will write in views.py.
# Thirdly, we are going to use a named parameter. This is going to be referenced in our templates in order to link from one page to another.
