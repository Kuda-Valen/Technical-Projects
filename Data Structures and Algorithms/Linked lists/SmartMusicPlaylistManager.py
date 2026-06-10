"""Smart Music Playlist Manager"""

class Media:
    def __init__(self, title: str, creator: str, duration: float):
        self.title = title
        self.creator = creator
        self.duration = duration

    def display_info():
        print("coming soon")

class Song(Media):
    def __init__(self, title: str, creator: str, duration: float, genre: str):
        super().__init__(title, creator, duration)
        self.genre = genre

class Podcast(Media): 
    def __init__(self, title: str, creator: str, duration: float, episode_num: int):
        super().__init__(title, creator, duration)
        self.episode_num = episode_num

class PlaylistNode: 
    def __init__(self, media_object, media_type):
        self.media_object = media_object
        self.media_type = media_type
        self.next = None
        
class PlaylistManager:
    def __init__(self):
        self.head = None
    
    def add_media(self):
        print("\n-- Add Media to Playlist --\n")
        print("1. Add a Song")
        print("2. Add a Podcast")
        try:
            option = int(input("\nChoose which media type you are adding: "))

            if option == 1:
                title = input("\nEnter title of Song: ")
                creator = input("Enter Creator's name: ")
                duration = 0.0
                try: 
                    duration = float(input("How long is it: "))
                except ValueError:
                    print("Duration only takes floats, using dot(.) format")

                genre = input("What genre is it: ")
                media_type = "song"

                media_info = Song(title, creator, duration, genre)
                media_object = PlaylistNode(media_info, media_type)
                
                if self.head is None:
                    self.head = media_object
                    return
        
                current = self.head

                while current.next:
                    current = current.next

                current.next = media_object
                

            elif option == 2:
                title = input("\nEnter Title of Podcast: ")
                creator = input("Enter Creator's name: ")
                duration = 0.0
                try:
                    duration = float(input("How long is it: "))
                except ValueError: 
                    print("Duration only takes floats, using dot(.) format")

                episode_num = input("which episode is it: ")
                media_type = "podcast"

                media_info = Podcast(title, creator, duration, episode_num)
                media_object = PlaylistNode(media_info, media_type)

                if self.head is None:
                    self.head = media_object
                    return
        
                current = self.head

                while current.next:
                    current = current.next

                current.next = media_object
            
            else: 
                print("Invalid Option: Choose a better option")
            
        except ValueError as e:
            print(f"\nInvalid input. Error: {e}")
        
    def view_playlist(self):
        print("\n-- Playlist --\n")
        if self.head is None:
            print("Your playlist is empty.")

        current = self.head

        while current:
            media = current.media_object
            if current.media_type == "song":
                print(f"Title: {media.title} | Creator: {media.creator} | Duration: {media.duration} | Genre: {media.genre}")
            
            elif current.media_type == "podcast":
                print(f"Title: {media.title} | Creator: {media.creator} | Duration: {media.duration} | Episode Number: {media.episode_num}")
            
            current = current.next
    
    def search_media(self):
        print("\n Seach Media")
        if self.head is None:
            print("There are no songs in the playlist")
            return
        
        target = input("Enter title to Search: ").lower()

        current = self.head

        while current.next:
            media = current.media_object
            if target == media.title.lower():
                if current.media_type == "song":
                    print(f"Title: {media.title} | Creator: {media.creator} | Duration: {media.duration} | Genre: {media.genre}")
                elif current.media_type == "podcast":
                    print(f"Title: {media.title} | Creator: {media.creator} | Duration: {media.duration} | Episode Number: {media.episode_num}")
            else:
                current = current.next
    
    def remove_media(self, title):
        print("delete node from linked list")
    
    def play_next(self):
        print("Removes first song from playlists queues")

if __name__ == "__main__":
    playlist_manager = PlaylistManager()

    print("\n<== Smart Music Playlist Manager ==>")

    while True: 
        
        print("\n1. Add Media to playlist")
        print("2. View Playlist")
        print("3. Search media in Playlist")
        print("4. Remove media from Playlist")
        print("5. Play Next")
        print("6. Exit..")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                playlist_manager.add_media()
            
            elif option == 2:
                playlist_manager.view_playlist()
            
            elif option == 3:
                playlist_manager.search_media()

            elif option == 6:
                print("\nExiting...")
                break

            else:
                print("Invalid Option. Choose a valid option")
        
        except ValueError as e: 
            print("Invalid input. Error: {e}")

"""
    NEXT IS TO FINISH THE OTHER FUCTIONS IN THE MENU
"""