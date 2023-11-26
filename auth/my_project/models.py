from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Country(db.Model):
    __tablename__ = 'country'
    country_id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(45), nullable=False)


class City(db.Model):
    __tablename__ = 'city'
    city_id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.country_id'), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    country = db.relationship('Country', backref=db.backref('cities', lazy=True))


class Region(db.Model):
    __tablename__ = 'region'
    region_id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'), nullable=False)
    region_name = db.Column(db.String(45), nullable=False)
    city = db.relationship('City', backref=db.backref('regions', lazy=True))


class User_new900(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email


class Users(db.Model):
    __tablename__ = "tblusers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, unique=True)
    email = db.Column(db.String(150), index=True, unique=True)
    password = db.Column(db.String(255), index=True, unique=True)


class Album(db.Model):
    __tablename__ = 'album'

    performer_id = db.Column(db.Integer, db.ForeignKey('performer.performer_id'), primary_key=True)
    song_id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, primary_key=True)
    album_name = db.Column(db.String(45), nullable=False)
    count_song = db.Column(db.Integer, nullable=False)

    # Define relationships
    performer = db.relationship('Performer', backref=db.backref('albums', lazy=True))


class MusicLabel(db.Model):
    __tablename__ = 'music_lable'

    music_lable_id = db.Column(db.Integer, primary_key=True)
    music_lable_name = db.Column(db.String(45), nullable=False)


class Performer(db.Model):
    __tablename__ = 'performer'

    performer_id = db.Column(db.Integer, primary_key=True)
    performer_name = db.Column(db.String(45), nullable=False)
    music_lable_id = db.Column(db.Integer, db.ForeignKey('music_lable.music_lable_id'), nullable=False)
    region_id = db.Column(db.Integer, nullable=False)

    # Define relationships
    music_label = db.relationship('MusicLabel', backref=db.backref('performers', lazy=True))
    # Assuming there is a Region model, you should define a relationship for it too
    # region = db.relationship('Region', backref=db.backref('performers', lazy=True))


class PlaylistHasSong(db.Model):
    __tablename__ = 'playlist_has_song'

    playlist_playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.playlist_id'), primary_key=True)
    song_song_id = db.Column(db.Integer, db.ForeignKey('song.song_id'), primary_key=True)

    # Змінено ім'я backref на 'playlist_has_song'
    playlist = db.relationship('Playlist', backref=db.backref('playlist_has_song', lazy=True))
    song = db.relationship('Song', backref=db.backref('playlist_has_song', lazy=True))


class Playlist(db.Model):
    __tablename__ = 'playlist'

    playlist_id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String(45), nullable=False)

    # Define relationships
    # songs = db.relationship('PlaylistHasSong', backref=db.backref('playlist', lazy=True))


class Song(db.Model):
    __tablename__ = 'song'

    song_id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String(45), nullable=False, index=True)
    genre = db.Column(db.String(45), nullable=False)
    release_date = db.Column(db.DateTime)
    # song_length = db.Column(db.Float)
    performer_id = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.album_id'), nullable=False)
    word_id = db.Column(db.Integer, nullable=False)

    # Define relationships
    # playlists = db.relationship('PlaylistHasSong', backref=db.backref('song', lazy=True))
