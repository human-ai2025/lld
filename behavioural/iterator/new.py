from collections.abc import Iterator, Iterable

class Song:
    def __init__(self, title: str):
        self.title = title
    def __str__(self): return self.title

# --- Concrete Iterator ---
class PlaylistIterator(Iterator):
    def __init__(self, songs: list):
        self._songs = songs
        self._position = 0

    # The __next__ method is the core of the iterator.
    def __next__(self) -> Song:
        try:
            song = self._songs[self._position]
            self._position += 1
        except IndexError:
            # When there are no more items, raise StopIteration.
            raise StopIteration()
        return song

# --- Concrete Aggregate (Collection) ---
class Playlist(Iterable):
    def __init__(self):
        self._songs = []

    def add_song(self, song: Song):
        self._songs.append(song)
    
    # The __iter__ method fulfills the "Iterable" contract.
    # It returns a new iterator object.
    def __iter__(self) -> PlaylistIterator:
        return PlaylistIterator(self._songs)

# --- Client Code ---
playlist = Playlist()
playlist.add_song(Song("Bohemian Rhapsody"))
playlist.add_song(Song("Stairway to Heaven"))

# The client code is now completely decoupled from the Playlist's internal storage.
# Python's for loop automatically calls __iter__() to get the iterator,
# and then calls __next__() on it until StopIteration is raised.
for song in playlist:
    print(f"Playing from classic iterator: {song}")
    
class PythonicPlaylist:
    def __init__(self):
        self._songs = []
    def add_song(self, song: Song):
        self._songs.append(song)
    
    # This __iter__ method is now a generator function.
    # It handles creating the iterator, managing state, and raising StopIteration implicitly.
    def __iter__(self) -> Iterator[Song]:
        for song in self._songs:
            yield song

# --- Client Code (remains identical) ---
pythonic_playlist = PythonicPlaylist()
pythonic_playlist.add_song(Song("Like a Rolling Stone"))
pythonic_playlist.add_song(Song("Smells Like Teen Spirit"))

for song in pythonic_playlist:
    print(f"Playing from pythonic iterator: {song}")