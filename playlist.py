liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    }
}
def name_song():
    NameSong = input("Enter name of the song: ")
    return NameSong
def artist_song():
    artist = input("Enter name of artist: ")
    return artist
def time_of_song():
    minute = int(input("Enter number of minutes: "))
    while minute < 0:
        minute = int(input("Enter number of minutes: "))
    second = int(input("Enter number of seconds: "))
    while second < 0 or second >59:
        second = int(input("Enter number of seconds: "))
    time = [minute,second]
    return tuple(time)
def genre_song():
    genre = input("Enter genre of the song: ")
    return genre
def add_to_dict(name,artist,time,genre):
    song_setting = {"artist": artist,"duration": time,"genre": genre}
    liked_songs[name] = song_setting
def remove_song():
    song = input("Enter song you're want to check if it in liked songs: ")
    not_in_list = True
    for i in liked_songs:
        if song.lower() == i.lower():
            print(f"{song} is in the list\ndo you want to remove this from the list")
            remove_or_not = input()
            not_in_list = False
            if remove_or_not.lower() == "yes":
                liked_songs.pop(i)
                break
    if not_in_list:
        print("Your song not in the list")
    print_liked_songs()
def remove_song_of_artist():
    artist = input("Which artist you want to remove all of his songs from your liked song list: ")
    counter_songs = 0
    for i in liked_songs:
        if liked_songs[i]["artist"].lower() == artist.lower():
            counter_songs += 1
    for counter in range(counter_songs):
        for song in liked_songs:
            if liked_songs[song]["artist"].lower() == artist.lower():
                liked_songs.pop(song)
                break
    if counter_songs == 0:
        print("Your artist not in the list")
    print_liked_songs()
def print_liked_songs():
    for i in liked_songs:
        print(f"{i}:\nThe artist: {liked_songs[i]["artist"]}\nThe duration: {liked_songs[i]["duration"]}\nThe genre: {liked_songs[i]["genre"]}")
    print()
def main():
    number_of_add = int(input("Enter how many songs you want to add:"))
    while number_of_add < 0:
        number_of_add = int(input("Enter how many songs you want to add:"))
    for i in range(number_of_add):
        name_of_song = name_song()
        artist = artist_song()
        time_song = time_of_song()
        genre = genre_song()
        add_to_dict(name_of_song,artist,time_song,genre)
    print_liked_songs()
    remove_song()
    remove_song_of_artist()
main()
