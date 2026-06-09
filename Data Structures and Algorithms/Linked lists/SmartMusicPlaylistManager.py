"""Smart Music Playlist Manager"""

class Media:
    def __init__(self, title: str, creator: str, duration: float):
        self.title = title
        self.creator = creator
        self.__duration = duration

    def display_info():
        print("coming soon")

class Song:
    def __init__(self, title: str, creator: str, duration: float, genre: str):
        super(Media).__init__(title, creator, duration)
        self.genre = genre

class Podcast: 
    def __init__(self, title: str, creator: str, duration: float, genre: str, episode_num: int):
        super(Media).__init__(title, creator, duration)
        self.episode_num = episode_num

class PlaylistNode: 
    def __init__(self):
        print("coming soon")
        
class PlaylistManager:
    def __init__(self):
        self.head = None