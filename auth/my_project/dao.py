# dao.py
from auth.my_project.models import db, Users, City, Performer, MusicLabel, Playlist, Song, PlaylistHasSong
from flask_marshmallow import Marshmallow
from flask import Flask, jsonify, request, Response
from auth.my_project.schema import user_schema, users_schema, \
    cities_schema, city_schema, performers_schema, music_labels_schema, \
    playlists_schema, songs_schema, playlist_song_schema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password_for_root@localhost/mydb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SECRET_KEY'] = 'cairocoders-ednalan'
SQLALCHEMY_ECHO = True

db.init_app(app)

with app.app_context():
    db.create_all()

ma = Marshmallow(app)


class UserDao:
    def get_all_labels_and_performers(self):
        all_labels = MusicLabel.query.all()
        results = music_labels_schema.dump(all_labels)

        for result in results:
            label_id = result['music_lable_id']
            performers = Performer.query.filter_by(music_lable_id=label_id)
            result['performers'] = [performer.performer_name for performer in performers]

        return results

    def get_all_playlist_song(self):
        all_playlist_songs = PlaylistHasSong.query.all()
        results = playlist_song_schema.dump(all_playlist_songs)

        for result in results:
            playlist_id = result['playlist_playlist_id']
            song_id = result['song_song_id']

            # Assuming you want to get song titles associated with the playlist
            songs = Song.query.join(PlaylistHasSong).filter_by(playlist_playlist_id=playlist_id).all()
            playlists = Playlist.query.join(PlaylistHasSong).filter_by(playlist_playlist_id=song_id).all()

            result['playlist'] = [playlist.playlist_name for playlist in playlists]
            result['songs'] = [song.song_title for song in songs]

            # Remove the old keys if needed
            result.pop('playlist_playlist_id', None)
            result.pop('song_song_id', None)

        return results

    # def get_all_playlist_song(self):
    #     all_users = PlaylistHasSong.query.all()
    #     results = playlist_song_schema.dump(all_users)
    #     return results

    def get_all_users(self):
        all_users = Users.query.all()
        results = users_schema.dump(all_users)
        return results

    def get_all_performers(self):
        all_users = Performer.query.all()
        results = performers_schema.dump(all_users)
        return results

    def get_all_labels(self):
        all_labels = MusicLabel.query.all()
        results = music_labels_schema.dump(all_labels)
        return results

    def get_all_playlist(self):
        all_playlist = Playlist.query.all()
        results = playlists_schema.dump(all_playlist)
        return results

    def get_all_song(self):
        all_song = Song.query.all()
        results = songs_schema.dump(all_song)
        return results

    def get_user_by_id(self, user_id):
        user = Users.query.get(user_id)
        return user_schema.dump(user)

    def get_all_cities(self):
        all_users = City.query.all()
        results = cities_schema.dump(all_users)
        return results

    def get_city_by_id(self, id):
        user = City.query.get(id)
        return city_schema.dump(user)

    def new_user(self):
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'Email already exists'}), 400

        users = Users(name=name, email=email, password=password)

        db.session.add(users)
        db.session.commit()
        serialized_user = user_schema.dump(users)

        if isinstance(serialized_user, Response):
            serialized_user = serialized_user.get_json()

        print(serialized_user)
        return serialized_user

    def new_city(self):
        city_id = request.json['city_id']
        country_id = request.json['country_id']
        name = request.json['name']

        users = City(city_id=city_id, country_id=country_id, name=name)

        db.session.add(users)
        db.session.commit()
        serialized_user = city_schema.dump(users)

        if isinstance(serialized_user, Response):
            serialized_user = serialized_user.get_json()

        print(serialized_user)
        return serialized_user

    def city_update(self, id):
        city = City.query.get(id)

        country_id = request.json['country_id']
        name = request.json['name']

        city.country_id = country_id
        city.name = name

        db.session.commit()
        return city_schema.dump(city)

    def city_delete(self, id):
        city = City.query.get(id)
        db.session.delete(city)
        db.session.commit()
        return city_schema.dump(city)

    def get_users_in_city(self, city_id):
        city = City.query.get(city_id)
        if city:
            users_in_city = city.users  # users - відношення, яке ви описали в моделі City
            results = users_schema.dump(users_in_city)
            return results
        else:
            return jsonify({'message': 'City not found'}), 404
