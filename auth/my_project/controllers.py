# controllers.py
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from auth.my_project.models import db, Users, Country, City, Region
from auth.my_project.services import UserService
from auth.my_project.db import app

app = Flask(__name__)
user_service = UserService()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password_for_root@localhost/mydb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SECRET_KEY'] = 'cairocoders-ednalan'
SQLALCHEMY_ECHO = True

CORS(app, supports_credentials=True)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/users', methods=['GET'])
def list_users():
    all_users = user_service.get_all_users()
    return jsonify(all_users)


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = user_service.get_user_by_id(id)
    return jsonify(user)


@app.route('/cities', methods=['GET'])
def list_cities():
    all_users = user_service.get_all_cities()
    return jsonify(all_users)


@app.route('/cities/<id>', methods=['GET'])
def get_city(id):
    user = user_service.get_city_by_id(id)
    return jsonify(user)


@app.route('/playlist', methods=['GET'])
def list_playlists():
    all_playlists = user_service.get_all_playlists()
    return jsonify(all_playlists)


@app.route('/performers', methods=['GET'])
def list_performers():
    all_users = user_service.get_all_performers()
    return jsonify(all_users)


@app.route('/songs', methods=['GET'])
def list_songs():
    all_songs = user_service.get_all_songs()
    return jsonify(all_songs)


@app.route('/playlist_song', methods=['GET'])
def list_playlist_songs():
    all_playlist_songs = user_service.get_all_playlist_song()
    return jsonify(all_playlist_songs)


@app.route('/music_labels', methods=['GET'])
def list_labels():
    all_labels = user_service.get_all_labels()
    return jsonify(all_labels)


@app.route('/music_labels_and_performers', methods=['GET'])
def list_labels_and_performers():
    all_data = user_service.get_all_labels_and_performers()
    return jsonify(all_data)


@app.route('/new_user', methods=['POST'])
def post_user():
    user = user_service.post_users()
    return (user)


@app.route('/new_city', methods=['POST'])
def post_city():
    city = user_service.post_cities()
    return (city)


@app.route('/city_update/<id>', methods=['PUT'])
def cityupdate(id):
    city_update = user_service.update_city(id)
    return jsonify(city_update)


@app.route('/city_delete/<id>', methods=['DELETE'])
def city_delete(id):
    citydel = user_service.delete_city(id)
    return jsonify(citydel)
