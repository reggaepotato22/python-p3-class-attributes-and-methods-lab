class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}  # Renamed from genre_counts
    artist_count = {} # Renamed from artist_counts

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song._increment_count()

        Song.add_genre(genre)

        Song.add_artist(artist)

        Song._update_genre_count(genre)
        Song._update_artist_count(artist)

    @classmethod
    def _increment_count(cls):
        cls.count += 1

    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def _update_genre_count(cls, genre):
        # Updated to use genre_count
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def _update_artist_count(cls, artist):
        # Updated to use artist_count
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_all_genres(cls):
        return cls.genres

    @classmethod
    def get_all_artists(cls):
        return cls.artists

    @classmethod
    def get_genre_counts(cls):
        # This method name remains get_genre_counts for external use,
        # but it now returns the content of the renamed genre_count attribute.
        return cls.genre_count

    @classmethod
    def get_artist_counts(cls):
        # This method name remains get_artist_counts for external use,
        # but it now returns the content of the renamed artist_count attribute.
        return cls.artist_count

if __name__ == "__main__":
    song1 = Song("Bohemian Rhapsody", "Queen", "Rock")
    song2 = Song("Stairway to Heaven", "Led Zeppelin", "Rock")
    song3 = Song("Shape of You", "Ed Sheeran", "Pop")
    song4 = Song("99 Problems", "Jay-Z", "Hip Hop")
    song5 = Song("Sweet Home Alabama", "Lynyrd Skynyrd", "Country")
    song6 = Song("Stairway to Heaven", "Led Zeppelin", "Rock")

    print(f"Total songs created: {Song.get_count()}")
    print(f"Unique genres: {Song.get_all_genres()}")
    print(f"Unique artists: {Song.get_all_artists()}")
    print(f"Songs per genre: {Song.get_genre_counts()}")
    print(f"Songs per artist: {Song.get_artist_counts()}")

    print(f"\nSong 1 details: {song1.name} by {song1.artist} ({song1.genre})")
    print(f"Song 4 details: {song4.name} by {song4.artist} ({song4.genre})")

    song7 = Song("Old Town Road", "Lil Nas X", "Country")
    print(f"\nAfter adding another song:")
    print(f"Total songs created: {Song.get_count()}")
    print(f"Unique genres: {Song.get_all_genres()}")
    print(f"Unique artists: {Song.get_all_artists()}")
    print(f"Songs per genre: {Song.get_genre_counts()}")
    print(f"Songs per artist: {Song.get_artist_counts()}")
