class Song:
    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        return self.title

class Playlist:
    def __init__(self):
        # The internal representation is a list
        self._songs = []

    def add_song(self, song: Song):
        self._songs.append(song)
    
    # This is the problem: we are exposing our internal list directly.
    def get_raw_songs(self) -> list:
        return self._songs

# --- Client Code ---
playlist = Playlist()
playlist.add_song(Song("Bohemian Rhapsody"))
playlist.add_song(Song("Stairway to Heaven"))
playlist.add_song(Song("Hotel California"))

# The client is tightly coupled to the fact that get_raw_songs() returns a list.
for song in playlist.get_raw_songs():
    print(f"Playing: {song}")

# If Playlist changes its internal storage from a list to a dictionary,
# the client's for loop will break.