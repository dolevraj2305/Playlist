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
    NameSong = input("Enter name song: ")
    return NameSong
def artist_song():
    artist = input("Enter name of artist: ")
    return artist
def time_of_song():
    minute = int(input("Enter number of minutes: "))
    second = int(input("Enter number of seconds: "))
    time = [minute,second]
    return tuple(time)
def genre_song():
    genre = input("Enter genre of the song: ")
    return genre
def add_to_dict(name,artist,time,genre):
    song_setting = {"artist": artist,"duration": time,"genre": genre}
    liked_songs[name] = song_setting
def print_liked_songs():
    for i in liked_songs:
        print(f"{i}:\nThe artist: {liked_songs[i][0]}\nThe duration: {liked_songs[i][1]}\nThe genre: {liked_songs[i][2]}")
    print()
def main():
    number_of_add = int(input("Enter how many songs you want to add"))
    for i in range(number_of_add):
        name_of_song = name_song()
        artist = artist_song()
        time_song = time_of_song()
        genre = genre_song()
        add_to_dict(name_of_song,artist,time_song,genre)
        print_liked_songs()
main()
