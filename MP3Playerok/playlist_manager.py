class PlaylistManager:
    def __init__(self):
        self.playlists = {}  # {"playlist_name": ["track1.mp3", "track2.mp3"]}

    def create_playlist(self, name):
        if not name:
            raise ValueError("Имя плейлиста не может быть пустым")
        if name in self.playlists:
            raise ValueError("Плейлист уже существует")
        self.playlists[name] = []
        return True

    def rename_playlist(self, old_name, new_name):
        if not new_name:
            raise ValueError("Новое имя плейлиста не может быть пустым")
        if old_name not in self.playlists:
            raise ValueError("Плейлист не существует")
        if new_name in self.playlists:
            raise ValueError("Плейлист с таким именем уже есть")
        self.playlists[new_name] = self.playlists.pop(old_name)
        return True

    def delete_playlist(self, name):
        if name not in self.playlists:
            raise ValueError("Плейлист не существует")
        del self.playlists[name]
        return True

    def add_track(self, playlist_name, track_path):
        if not track_path:
            raise ValueError("Трек не выбран")
        if playlist_name not in self.playlists:
            raise ValueError("Плейлист не существует")
        self.playlists[playlist_name].append(track_path)
        return True