from rest_framework import serializers
from .models import Artist, Song


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        view_name='song_detail',
        many=True,
        read_only=True
    )
    # We also want to describe all the fields in artist. We'll do this using a Meta class.

    class Meta:
        model = Artist
        fields = ('id', 'photo_url', 'nationality', 'name', 'songs',)


class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    )

    class Meta:
        model = Song
        # You can also use "all" in your fields to simply take all of them.
        fields = ('id', 'artist', 'title', 'album', 'preview_url',)

#    We are creating a HyperlinkedRelatedField and pointing it to the song_detail view. This allows us to link one model to another using a hyperlink. So when we inspect the json response, we'll be able to just follow a url that takes us to from the current Artist to the related Song.

# The Meta class within our Artist serializer class specifies meta data about our serializer. In this class, we tell it the model and what fields we want to serialize.

# The view_name specifies the name of the view given in the urls.py file. If we look at our tunr/urls.py file, we already have a path like this: path('songs/<int:pk>', views.song_detail, name='song_detail')


# Serializers allow us to convert our data from QuerySets (the data type returned by Django's ORM) to data that can easily be converted to JSON (or XML) and returned by our API. There are several types of serializers built into Django REST framework; however, we will be using the HyperlinkedModelSerializer today. This serializer allows us to specify model fields that we want to include in our API and it will generate our JSON accordingly. It will also allow us to link from one model to another.
