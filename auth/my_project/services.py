# services.py
from auth.my_project.dao import UserDao


class UserService:
    def __init__(self):
        self.user_dao = UserDao()

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def get_all_performers(self):
        return self.user_dao.get_all_performers()

    def get_all_labels(self):
        return self.user_dao.get_all_labels()

    def get_all_playlists(self):
        return self.user_dao.get_all_playlist()

    def get_all_songs(self):
        return self.user_dao.get_all_song()

    def get_all_playlist_song(self):
        return self.user_dao.get_all_playlist_song()

    def get_all_labels_and_performers(self):
        return self.user_dao.get_all_labels_and_performers()

    def get_user_by_id(self, user_id):
        return self.user_dao.get_user_by_id(user_id)

    def get_all_cities(self):
        return self.user_dao.get_all_cities()

    def get_city_by_id(self, user_id):
        return self.user_dao.get_city_by_id(user_id)

    def post_users(self):
        return self.user_dao.new_user()

    def post_cities(self):
        return self.user_dao.new_city()

    def update_city(self, id):
        return self.user_dao.city_update(id)

    def delete_city(self, id):
        return self.user_dao.city_delete(id)
