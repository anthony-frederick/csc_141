# Lets the user input an artist and ine of their songs

def make_album(artist, album):
    """Returns a dictionary of an artist and their album"""
    info = {'name': artist, 'album': album}
    return info
name_prompt = ("Please enter the name of the artist: ")
album_prompt = ("Please neter the name of the album: ")
print("Enter q at any time to quit")
while True:
    artist = input(name_prompt)
    if artist == 'q':
        break
    album = input(album_prompt)
    if album == 'q':
        break
    artist_album = make_album(artist, album)
    print(artist_album)
print("\nThanks for responding!")