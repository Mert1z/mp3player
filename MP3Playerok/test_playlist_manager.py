import unittest
from playlist_manager import PlaylistManager

class TestPlaylistManager(unittest.TestCase):
    def setUp(self):
        self.manager = PlaylistManager()

    def test_create_playlist_success(self):
        self.assertTrue(self.manager.create_playlist("Rock"))

    def test_create_playlist_empty_name(self):
        with self.assertRaises(ValueError):
            self.manager.create_playlist("")

    def test_create_playlist_duplicate(self):
        self.manager.create_playlist("Pop")
        with self.assertRaises(ValueError):
            self.manager.create_playlist("Pop")

    def test_rename_playlist_success(self):
        self.manager.create_playlist("OldName")
        self.assertTrue(self.manager.rename_playlist("OldName", "NewName"))

    def test_delete_playlist_success(self):
        self.manager.create_playlist("ToDelete")
        self.assertTrue(self.manager.delete_playlist("ToDelete"))

    def test_add_track_success(self):
        self.manager.create_playlist("MyPlaylist")
        self.assertTrue(self.manager.add_track("MyPlaylist", "song.mp3"))

    def test_add_track_invalid_playlist(self):
        with self.assertRaises(ValueError):
            self.manager.add_track("Unknown", "song.mp3"))

if __name__ == "__main__":
    unittest.main()