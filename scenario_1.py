class Song:
    def __init__(self, title):
        self.title = title
        self.next = None

class Songs:
    def __init__(self):
        self.head = None

    def add_song_at_beginning(self, title):
        new_song = Song(title)

        if self.head is None:
            self.head = new_song
            print("Song added successfully!\n")
            return

        new_song.next = self.head
        self.head = new_song

        print("Song added successfully!\n")

    def add_song_at_end(self, title):
        new_song = Song(title)

        if self.head is None:
            self.head = new_song
            print("Song added successfully!\n")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_song

        print("Song added successfully!\n")

    def add_song_at_position(self, title, pos):
        if pos <= 0:
            print("Invalid position!\n")
            return

        if pos == 1:
            self.add_song_at_beginning(title)
            return

        new_song = Song(title)

        i = 1
        temp = self.head

        while i < pos - 1 and temp is not None:
            temp = temp.next
            i += 1

        if temp is None:
            print("Songs are less than the specified position!\n")
            return

        new_song.next = temp.next
        temp.next = new_song

        print("Song added successfully!\n")

    def remove_song_from_beginning(self):
        if self.head is None:
            print("No songs in the playlist!\n")
            return

        self.head = self.head.next

        print("Song removed successfully!\n")

    def remove_song_from_end(self):
        if self.head is None:
            print("No songs in the playlist!\n")
            return

        if self.head.next is None:
            self.head = None
            print("Song removed successfully!\n")
            return

        prev = None
        temp = self.head

        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = None

        print("Song removed successfully!\n")

    def remove_song_from_position(self, pos):
        if self.head is None:
            print("No elements in the list!\n")
            return

        if pos <= 0:
            print("Invalid position!\n")
            return

        if pos == 1:
            self.head = self.head.next
            print("Song removed successfully!\n")
            return

        i = 1
        prev = None
        temp = self.head

        while i < pos and temp is not None:
            prev = temp
            temp = temp.next
            i += 1

        if temp is None:
            print("Songs are less than the specified position!\n")
            return

        prev.next = temp.next

        print("Song removed successfully!\n")

    def search_song_in_playlist(self, song):
        if self.head is None:
            return "No songs in the playlist!\n"

        temp = self.head
        pos = 1

        while temp is not None:
            if temp.title == song:
                return f"'{song}' found at position {pos}\n"

            temp = temp.next
            pos += 1

        return f"'{song}' not found in the playlist!\n"

    def get_length_of_playlist(self):
        if self.head is None:
            return 0

        length = 1
        temp = self.head

        while temp.next is not None:
            temp = temp.next
            length += 1

        return length

    def display_playlist(self):
        if self.head is None:
            print("No songs in the list!\n")
            return

        temp = self.head

        print("Playlist:")
        
        while temp is not None:
            print(temp.title, end=" -> ")
            temp = temp.next
        print("NULL")

    def reverse_playlist(self):
        if self.head is None:
            print("No songs in the playlist!\n")
            return

        if self.head.next is None:
            print("Only one song in the playlist!\n")
            return

        prev = None
        curr = self.head

        while curr is not None:
            temp=curr.next

            curr.next = prev
            prev = curr
            curr=temp

        self.head = prev

        print("Playlist reversed successfully!\n")

songs = Songs()

print("\n================================")
print("YOUR PERSONALIZED MUSIC PLAYLIST")
print("================================\n")

while True:
    print("Menu:")
    print("1. Add a song to the beginning of the playlist")
    print("2. Add a song to the end of the playlist")
    print("3. Insert a song at a specified position")
    print("4. Remove the first song from the playlist")
    print("5. Remove the last song from the playlist")
    print("6. Remove the song at a specified position")
    print("7. Search for a song and display its position")
    print("8. Display the total number of songs")
    print("9. Display the complete playlist")
    print("10. Reverse the playlist order")
    print("11. Exit the application")

    choice = int(input("\nEnter your choice (1-11): "))

    match choice:
        case 1:
            song = input("Enter song you want to add: ")
            songs.add_song_at_beginning(song)

        case 2:
            song = input("Enter song you want to add: ")
            songs.add_song_at_end(song)

        case 3:
            song = input("Enter song you want to add: ")
            position = int(input("Enter position where you want to add song: "))
            songs.add_song_at_position(song, position)

        case 4:
            songs.remove_song_from_beginning()

        case 5:
            songs.remove_song_from_end()

        case 6:
            position = int(input("Enter position of song you want to delete: "))
            songs.remove_song_from_position(position)

        case 7:
            song = input("Enter song you want to search: ")
            print(songs.search_song_in_playlist(song))

        case 8:
            print(f"Total songs in the playlist: {songs.get_length_of_playlist()}")

        case 9:
            songs.display_playlist()

        case 10:
            songs.reverse_playlist()
            songs.display_playlist()

        case 11:
            print("\nApplication exited successfully!")
            break