

        

def make_album(artist_name, album_title, number_of_songs= None): 
    music_album = {"artist_name": artist_name, "album_title": album_title}
    if number_of_songs:
        music_album["number_of_songs"] = number_of_songs
    print(music_album)

    
make_album("happy", "philip")
make_album ("hello", "adele",30)


