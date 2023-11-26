from flask_marshmallow import Marshmallow
from auth.my_project.db import app

ma = Marshmallow(app)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class CountrySchema(ma.Schema):
    class Meta:
        fields = ('country_id', 'country_name')


country_schema = CountrySchema()
countries_schema = UserSchema(many=True)


class CitySchema(ma.Schema):
    class Meta:
        fields = ('city_id', 'country_id', 'name')


city_schema = CitySchema()
cities_schema = CitySchema(many=True)


class RegionSchema(ma.Schema):
    class Meta:
        fields = ('region_id', 'city_id', 'region_name')


regions_schema = RegionSchema(many=True)
region_schema = RegionSchema()


class AlbumSchema(ma.Schema):
    class Meta:
        fields = ('performer_id', 'song_id', 'album_id', 'album_name', 'count_song')


albums_schema = RegionSchema(many=True)
album_schema = RegionSchema()


class MusicLabelSchema(ma.Schema):
    class Meta:
        fields = ('music_lable_id', 'music_lable_name', 'performers')

    performers = ma.List(ma.String)


music_labels_schema = MusicLabelSchema(many=True)
music_label_schema = MusicLabelSchema()


class PerformerSchema(ma.Schema):
    class Meta:
        fields = ('performer_id', 'performer_name', 'music_lable_id', 'region_id')


performers_schema = PerformerSchema(many=True)
performer_schema = PerformerSchema()


class SongSchema(ma.Schema):
    class Meta:
        fields = ('song_id', 'song_title', 'genre', 'release_date',
                  'performer_id', 'album_id', 'word_id')


songs_schema = SongSchema(many=True)
song_schema = SongSchema()


class PlaylistSchema(ma.Schema):
    class Meta:
        fields = ('playlist_id', 'playlist_name')


playlists_schema = PlaylistSchema(many=True)
playlist_schema = PlaylistSchema()


class PlaylistHasSongSchema(ma.Schema):
    class Meta:
        fields = ('playlist_playlist_id', 'song_song_id')
        # playlist_playlist_id = ma.List(ma.String)
        # song_song_id = ma.List(ma.String)


playlist_song_schema = PlaylistHasSongSchema(many=True)
