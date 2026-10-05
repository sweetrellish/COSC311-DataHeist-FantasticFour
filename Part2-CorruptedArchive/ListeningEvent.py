"""Class declaration for ListeningEvent object from Part 1 that links a Listener and 
Song together, with attributes listener, song, timestamp (i.e. "2026-03-14 21:05"),
and seconds_played."""

class ListeningEvent():
    def __init__(self, listener, song,_title, artist, timestamp, seconds_played):
        self.listener = listener
        self.song = song
        self._title = _title
        self.artist = artist
        self.timestamp = timestamp
        self.seconds_played = seconds_played


